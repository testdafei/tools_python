# -*- coding: utf-8 -*-
"""
抖音商品口令转正常 URL 链接
支持：纯口令文本、已包含 v.douyin.com 的文本
会解析短链重定向，返回可正常打开商品的最终 URL
可在工作流中通过 async main(params) 调用，入参为口令字符串或包含口令的字典。
"""

import re
import ssl
from typing import Optional
from urllib.parse import parse_qs, unquote, urlparse
from urllib.request import Request, build_opener, HTTPSHandler
from urllib.error import URLError, HTTPError


def extract_douyin_url(text: str) -> Optional[str]:
    """
    从文本中提取或解析出抖音链接。
    若文本里已有 v.douyin.com 短链则直接提取，否则从口令中解析短码并拼成链接。
    """
    if not text or not text.strip():
        return None

    text = text.strip()

    # 1. 已包含 v.douyin.com 短链：直接提取
    # 匹配 https://v.douyin.com/xxx/ 或 v.douyin.com/xxx
    short_link = re.search(
        r'(?:https?://)?v\.douyin\.com/([A-Za-z0-9_-]+)/?',
        text,
        re.IGNORECASE
    )
    if short_link:
        code = short_link.group(1)
        return f"https://v.douyin.com/{code}/"

    # 2. 口令文本：提取短码（通常为 8~20 位字母数字）
    # 口令中短码常出现在「详情」附近或整段中的连续字母数字
    # 先尝试匹配「详情」后的短码
    after_detail = re.search(
        r'[详情页]+\s*[▽◆●\s]*([A-Za-z0-9]{8,20})',
        text
    )
    if after_detail:
        code = after_detail.group(1)
        return f"https://v.douyin.com/{code}/"

    # 再尝试匹配整段中较长的连续字母数字（排除纯数字，因可能是其他编号）
    # 抖音短码一般含字母
    candidates = re.findall(r'[A-Za-z][A-Za-z0-9]{7,19}|[A-Za-z0-9]{8,20}[A-Za-z]', text)
    if candidates:
        # 取最像短码的：长度适中、含字母
        for c in candidates:
            if re.search(r'[A-Za-z]', c) and 8 <= len(c) <= 20:
                return f"https://v.douyin.com/{c}/"

    return None


# 模拟浏览器，避免被抖音识别为脚本
_DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


# 最终结果规则：必须为以下格式，浏览器可打开
# 示例：https://haohuo.jinritemai.com/ecommerce/trade/detail/index.html?id=3772702387010142542&origin_type=604
_JINRITEMAI_PRODUCT_URL = "https://haohuo.jinritemai.com/ecommerce/trade/detail/index.html?id={commodity_id}&origin_type=604"


def _extract_https_from_aweme_location(location: str) -> Optional[str]:
    """从 302 Location（aweme://...?url=xxx）中解析出真正的 https 商品页 URL。"""
    if not location or not location.strip().startswith("aweme://"):
        return None
    idx = location.find("?")
    if idx == -1:
        return None
    query = location[idx + 1 :]
    params = parse_qs(query, keep_blank_values=True)
    if "url" not in params:
        return None
    raw = params["url"][0]
    # 可能有多层编码，解码到稳定
    for _ in range(3):
        decoded = unquote(raw)
        if decoded == raw:
            break
        raw = decoded
    if raw.startswith("https://") or raw.startswith("http://"):
        return raw
    return None


def _extract_product_id_from_url(url: str) -> Optional[str]:
    """
    从商品页 URL 的查询参数中提取商品 ID，用于拼详情页链接。
    部分链接只有 commodity_id，部分只有 promotion_id，兼容两种。
    若 URL 中含 #（如 web_bg_color=#ffffff），urlparse 会把 # 后当 fragment 导致参数丢失，
    故先用 parse_qs，没有则用正则从整段 URL 中匹配 commodity_id 或 promotion_id。
    """
    parsed = urlparse(url)
    params = parse_qs(parsed.query, keep_blank_values=True)
    for key in ("commodity_id", "promotion_id"):
        vals = params.get(key)
        if vals and vals[0]:
            return vals[0]
    # URL 中可能出现 web_bg_color=#ffffff，导致 # 后内容被当作 fragment，用正则从整段 URL 匹配
    for key in ("commodity_id", "promotion_id"):
        m = re.search(r"[?&]" + re.escape(key) + r"=(\d+)", url)
        if m:
            return m.group(1)
    return None


def resolve_short_url(short_url: str, timeout: int = 10) -> str:
    """
    请求短链，从 302 的 Location 解析出 commodity_id，
    返回浏览器可打开的抖店商品详情页 URL（haohuo.jinritemai.com）。
    """
    req = Request(short_url, headers=_DEFAULT_HEADERS)

    def _open(ctx: ssl.SSLContext):
        opener = build_opener(HTTPSHandler(context=ctx))
        return opener.open(req, timeout=timeout)

    def _parse_location(location: str) -> str:
        inner_url = _extract_https_from_aweme_location(location)
        if not inner_url:
            raise ValueError(f"短链 302 的 Location 中未解析出 https 链接: {location[:200]}...")
        # 兼容 commodity_id 与 promotion_id（部分商品只带 promotion_id）
        pid = _extract_product_id_from_url(inner_url)
        if not pid:
            raise ValueError("解析结果中未找到 commodity_id 或 promotion_id，无法生成标准商品详情页链接。")
        # 严格按规则输出：haohuo.jinritemai.com/ecommerce/trade/detail/index.html?id=xxx&origin_type=604
        return _JINRITEMAI_PRODUCT_URL.format(commodity_id=pid)

    ssl_ctx = ssl.create_default_context()
    try:
        _open(ssl_ctx)
    except HTTPError as e:
        if e.code != 302:
            raise ValueError(f"短链解析失败（非 302）: {e}") from e
        location = e.headers.get("Location") or e.headers.get("location") or ""
        return _parse_location(location)
    except OSError as e:
        if "CERTIFICATE_VERIFY_FAILED" in str(e) or "SSL" in str(e):
            ssl_ctx = ssl._create_unverified_context()
            try:
                _open(ssl_ctx)
            except HTTPError as e2:
                if e2.code == 302:
                    location = e2.headers.get("Location") or e2.headers.get("location") or ""
                    return _parse_location(location)
                raise ValueError(f"短链解析失败: {e2}") from e2
            except (URLError, OSError) as e2:
                raise ValueError(f"短链解析失败（网络或重定向异常）: {e2}") from e2
        raise ValueError(f"短链解析失败（网络或重定向异常）: {e}") from e
    except URLError as e:
        raise ValueError(f"短链解析失败（网络或重定向异常）: {e}") from e
    raise ValueError("短链未返回 302，无法解析")


async def main(params):
    """
    工作流入口：入参为口令字符串或字典（如 {"command": "口令"}）。
    返回 {"url": "可打开的抖店商品详情页 URL", "success": True} 或 {"success": False, "error": "错误信息"}。
    """
    try:
        if isinstance(params, str):
            command = params.strip()
        elif isinstance(params, dict):
            command = (
                params.get("command")
                or params.get("text")
                or params.get("input")
            )
            if command is None and len(params) == 1:
                command = next(iter(params.values()))
            command = str(command).strip() if command is not None else ""
        else:
            command = str(params).strip()
        if not command:
            return {"success": False, "error": "入参为空，请传入抖音商品口令字符串"}
        url = command_to_url(command)
        return {"success": True, "url": url}
    except ValueError as e:
        return {"success": False, "error": str(e)}
    except Exception as e:
        return {"success": False, "error": f"解析异常: {e}"}


def command_to_url(command: str, resolve_redirect: bool = True) -> str:
    """
    将抖音商品口令转为可打开的 URL。
    - resolve_redirect=True 时，会解析短链得到最终落地页 URL（推荐，可正常打开商品）。
    - resolve_redirect=False 时，仅返回 v.douyin.com 短链。
    若无法解析则抛出 ValueError。
    """
    url = extract_douyin_url(command)
    if not url:
        raise ValueError("无法从输入文本中解析出抖音链接，请检查是否为有效的商品口令或短链文本。")
    if resolve_redirect and "v.douyin.com" in url:
        url = resolve_short_url(url)
    return url


if __name__ == "__main__":
    # 示例
    examples = [
        '5 X@M.Ji 12/19 【Mexican/稻草人重磅纯棉水洗工:/ 装夹克男春季新款宽松痞帅休闲外套】复制此条消息打开抖音，查看商品详情。【※※34pxWzKuNe49ǚǚ】	 https://v.douyin.com/NrP1ph4AeuI/',
        '6:/ 05/09 g@b.nd 【花花公子夹克男新款休闲冲锋衣秋衣男装秋季风衣套装男士秋装外套】复制此条消息打开抖音，查看商品详情。【^^yvMryGHbeg49ǚǚ】	 https://v.douyin.com/2ysr5MHetlU/',
        '8:/ T@y.TL 04/03 【【内胆可拆卸】皮尔卡丹三合一冲锋衣男士户外登山加绒加厚夹克外套】复制此条消息打开抖音，查看商品详情。【ŠŠoxJYUXMeg49︽︽】	 https://v.douyin.com/DMRzTdbYysk/',
        '0X:/- S@Y.mQ 04/13 【Mexican/稻草人重磅纯棉水洗工装夹克男春季新款宽松痞帅休闲外套】复制此条消息打开抖音，查看商品详情。【ˇˇoBo4nQtNbyVh49※※】	 https://v.douyin.com/J8cooH0sMbE/',
        '1 q@e.bN 07/09 【Mexican/稻草人重磅纯棉水洗工装夹克男春季新款宽松痞帅休闲外套】复制此条消息打开抖音，查看:/ 商品详情。【※※s2wut4zWVh49※※】	 https://v.douyin.com/nhwxGOtI2Fc/',
        
    ]

    print("抖音商品口令 → URL\n" + "=" * 50)
    for raw in examples:
        try:
            url = command_to_url(raw)
            print(f"输入: {raw[:50]}...")
            print(f"链接: {url}\n")
        except ValueError as e:
            print(f"输入: {raw[:50]}...")
            print(f"错误: {e}\n")
