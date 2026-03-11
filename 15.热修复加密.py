import requests
import json

code = """
{"patch_version":"82752a2709124b0da1439130123d4fe9","download_url":"https://inf-cdn.wtzw.com/hotfix/test/patch/1705037558136_2134655460553796.jar","md5":"7fde6879c2be447295383a17b5e19f53","trace_id":"8d2ac7fd-6afb-4352-9b55-9ace48ccc721"}
"""

code = code.strip()

result = requests.post(
    url='https://key-secret-toolkit-wbddiplpzu.cn-shanghai.fcapp.run/encrypt',
    headers={
            "X-Fc-Invocation-Code-Version": "Latest",
            "X-Fc-Log-Type": "Tail",
            "content-type": "application/json"
        },
    json={
            # config_center-配置中心数据  drs-客户端离线日志  rtlrs-客户端实时日志  lrs-服务端通用日志  frontend-前端埋点日志（包括快应用，小程序）
            "app": "config_center",
            # "app": "drs",

            # test-测试环境  prod-生产环境
            "env": "prod",


            # 项目名  具体见http://wiki.km.com/pages/viewpage.action?pageId=50598885
            # "project_name": "reader_free_ios",
            "project_name": "reader_free",

            # 未加密数据
            "data": code
}
).json()

print(result['data'])