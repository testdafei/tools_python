import json
from hashlib import md5
import base64

# qmparams解密
qmparams = "cLGeuyoMmqN6OlNDOzf5A5HwtTFENI0wNT4lAhFLNh-lNIglH5w5uCR1paHWHT9wgI9wgI9wth9Y4h9QglFLpaMwgI9wth9wgI9wgI9wgI9wgaHjHzk2uz2Tp3U1paHWHTHwgT0wNTHrgh4LgeFlAh4Lgyfwgeux4T9wgeo2Nex-4eu-Nh-eNIoTNlkxpz0wghgUgqoxgqFrpI-ENygrH5w5BqoTHTZ5FTHWNh0WNIHWgIFWFTgWgh45taGeBERL4lRUmqF5A5HwNTgwpq0EAaMYgzfMthkzNqgQAyR2NLMlgqHe4efnpI9E4T45taGecCgQuzRLHTZ5gh95taGMOSReuyR-tq2-HTZ5koRkh0pkAfQyOqfLpqZUBlYQNyuDhhkGfMkThzkf3RR5thfUf-pqf2koq2G8RCk_4UuRcR1CBeo5gTRMh-u-u2kff-1RgoGVRyU3RRNqRz2gRofn4eGZg3HjHSsZBlY2tqn2uzRjHTZ53aHjHz2Qpq-5A5H5taGQBlk2BaHWH2NFh5UshI9wH5w5uln5tq2Qpq-5A5H5taGEByHQuq2-HTZ54zo24TN-4TgQpIRz4LMMNh9wtq0LpyfQNIx5gyfE4hxxgyG2H5w54ln1pqYMtq2-HTZ5AIHlAh0Lgh9egyoz4l0n43HjHzGL4qY-HTZ53oRsRMRGH5w5Blo1paHWHzGxpqHepyHetqFUpzgQNIfwgaUxgzk2thFr4Ts2Nl0r4hs5p3GJ"

s = "9saI0oy_HGitgNA8Fk3hfRqC4pmBOuc6Kx5T-2zSZ1VvjQ7DwnLeMUlErYWbdJPX"
bin_str = []

for i in qmparams:
    if i != '=':
        x = str(bin(s.index(i))).replace('0b', '')
        bin_str.append('{:0>6}'.format(x))
# print(bin_str)
# 输出的字符串
outputs = ""
nums = qmparams.count('=')
while bin_str:
    temp_list = bin_str[:4]
    temp_str = "".join(temp_list)
    # print(temp_str)
    # 补足8位字节
    if (len(temp_str) % 8 != 0):
        temp_str = temp_str[0:-1 * nums * 2]
    # 将四个6字节的二进制转换为三个字符
    for i in range(0, int(len(temp_str) / 8)):
        outputs += chr(int(temp_str[i * 8:(i + 1) * 8], 2))
    bin_str = bin_str[4:]
outputs = json.loads(outputs)
print(json.dumps(outputs, indent=4))
print('*'*20)

# 原始的请求参数，格式请参考
# {"device-id":"BIeIK39T+0BJVlayU6bKRs88Cf05uG54LQBmVOx4Dho3gO\/j0Gtc6KfMlAf0hLO36vpi5TTc4TOGYFcUAtiBROQ==","uuid":"4FB92A8C-5719-46EC-BA7B-BC489F1B2261","imei":"4FB92A8C-5719-46EC-BA7B-BC489F1B2261","wlb-imei":"4FB92A8C-5719-46EC-BA7B-BC489F1B2261","brand":"Apple","trusted-id":"D2j15OwH7c3Hbw2UpK2HdOEadxuTeqiwsMNqLWQSGl8jsX07","idfa":"4FB92A8C-5719-46EC-BA7B-BC489F1B2261","client-id":"","model":"iPhone8,1","sys-ver":"12.7","mac":""}

qm_params_original_str = """
{
    "uuid": "00000000-09a0-3d2d-0000-000000000000",
    "device-id": "",
    "mac": "32:0A:6A:F1:85:68",
    "sourceuid": "0630ea78-92e4-4f5c-8ee7-61b3c51d07b6",
    "sys-ver": "10",
    "trusted-id": "DUQLFQ9KFqe2ej5onm4goM4ISDcNdTIUb-55RFVRTEZROUtGcWUyZWo1b25tNGdvTTRJU0RjTmRUSVViLTU1c2h1",
    "imei": "",
    "model": "SPN-AL00",
    "wlb-imei": "",
    "wlb-uid": "baeb3db3-d5fc-4500-a2de-48b0e7a8a0be",
    "client-id": "8269121030afca1a",
    "brand": "HUAWEI",
    "oaid": "baeb3db3-d5fc-4500-a2de-48b0e7a8a0be"
}
"""
qm_params_original_str = qm_params_original_str.strip().replace(' ', '').replace('\n', '').replace('\r', '')
s = "9saI0oy_HGitgNA8Fk3hfRqC4pmBOuc6Kx5T-2zSZ1VvjQ7DwnLeMUlErYWbdJPX"

bin_str = []
for i in qm_params_original_str:
    x = str(bin(ord(i))).replace('0b', '')
    bin_str.append('{:0>8}'.format(x))
outputs = ""
nums = 0
while bin_str:
    temp_list = bin_str[:3]
    if (len(temp_list) != 3):
        nums = 3 - len(temp_list)
        while len(temp_list) < 3:
            temp_list += ['0' * 8]
    temp_str = "".join(temp_list)
    temp_str_list = []
    for i in range(0, 4):
        temp_str_list.append(int(temp_str[i * 6:(i + 1) * 6], 2))
    if nums:
        temp_str_list = temp_str_list[0:4 - nums]

    for i in temp_str_list:
        outputs += s[i]

    bin_str = bin_str[3:]
outputs += nums * '='
print("Encrypted String:\n%s" % outputs)
print('*'*20)

def string_to_md5(string):
    """
    字符串md5
    :param string:
    :return:
    """
    m = md5()
    m.update(string.encode("utf-8"))
    str_md5 = m.hexdigest()
    return str_md5

def str_to_json(string):
    headers = string.strip().split('\n')
    data_json = {}
    for i in headers:
        data = i.split(':')
        data_json.update({data[0].strip(): data[1].strip()})

    return data_json

# 接口header，可用fiddler复制出来，格式保持一致
headers = '''
net-env: 1
channel: unknown
is-white: 0
platform: android
app-version: 51580
reg: 3030996534
application-id: com.kmxs.reader
AUTHORIZATION: eyJhbGciOiJSUzI1NiIsImNyaXQiOlsiaXNzIiwianRpIiwiaWF0IiwiZXhwIl0sImtpZCI6IjE1MzEyMDM3NjkiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2MjgyNDkxNTUsImlhdCI6MTYyNTY1NzE1NSwiaXNzIjoiaHR0cHM6Ly94aWFvc2h1by53dHp3LmNvbS9hcGkvdjEvbG9naW4vaW5kZXgiLCJqdGkiOiIyNDlmNWQxM2QxMzMzMWRkNDA2MDY5ZDJmNDNjMTFiYSIsInVzZXIiOnsidWlkIjo1MDAwMDEwODUsIm5pY2tuYW1lIjoi5LiD54yr5Lmm5Y-LXzA3MDc0ODk3OTg1NyIsImltZWkiOiIiLCJ1dWlkIjoiMDAwMDAwMDAtNGFiMS03NTdkLTAwMDAtMDAwMDAwMDAwMDAwIiwiZGV2aWNlSWQiOiIyMDIxMDcwNzIwMjQ1MzQ3YjUyMjUyNjE0OGMyZmRmOWU2MTJmZjQzNzUxYjk2MDBjNGMwYWRmNTk3N2ZmYSIsInJlZ1RpbWUiOjE2MjU2MzU5NTIsInZpcEV4cGlyZUF0IjowLCJzbV9pZCI6IjIwMjEwNzA3MTQyOTE2NmYxZmU2ODZjMjAwZGEwODIzYWUyYTQ5ZDNhZjc3ZTcwMDlkZTlhOWRkZDk1MDRjIiwibnV0IjowLCJpZnUiOjAsImlzX3JiZiI6MCwiYWN0X2lkIjowLCJiaW5kX2F0IjowfX0.YeRzxJiUAeacQ_DCGtL8a6eDPSOMKqCpN0BAHJ9WCPe819fYCD-0iMNC9IRhKXE64v8zUWyZspkHlIAjYrSV7TPEtBSBRQfko6TpPaXFSEQ47y56XDQ_0Suv-LVjPi5LujcrRWC0KlJ5xaUNDyZIWtWNo8CT87S5-hgFRcs3ou0
qm-params: cLGZ4CG-uloLp3U1paHWHT9wgI9wgI9wth9nph-QAI0rp3Uzpzpztqpzpzp2pT9U4qgM43HjHSRUmqF5A5HwgI9wgI9wgaMM4qHnthOUNlFQgI9wgaMwgI9wgI9wgI9wgI95taG-pCp14lfQmqF5A5HLgIHngIHLgT0egegnAqk54egENIxxNh254eOrgl0r4qHe4eR2NhKn4hu-Ah25gIo5gI4LNeGxNT9egToTpaHjHzUx4LHWH-NsAT2sA-fnATkoAT4UAT4eH5w5OE2etCp2O5HWHT0nH5w5u_GUOEk2paU1paHWH-kU3eovNfQsNhHYfSpIp0NgcTGru0RLgfJSF-JIRlUfmf2h3Uk-O0UvR-pqhou-O_u2BqdDpquLfzQY3Eujh0RGR0QaOo4EtlJSO2N2BMxehEKYNMwMgo05taG1BqR1HTZ5H5w5BqJ-pqw5A5G3pqkQm3stgT9Kf_GDH5w5uln5tq2Qpq-5A5H5taGEByHQuq2-HTZ5pqNTghszNTkzNT-eghfMNLHjHzNjmqR7uaU1paHWHTu5NqHMNIKMNIgUgIHMNqH5taG5Ozo7paHWH2x14qJQm3HjHzJxmqF5A5G24lgngy4lNy4lAhgnNhFEHSM=
sign: da23f48d57972197d2056f9d8e258225
QM-it: 1625207214
QM-ii: 3030996534
no-permiss: 0
User-Agent: webviewversion/51580
Host: xiaoshuo.wtzw.com
Connection: Keep-Alive
Accept-Encoding: gzip
If-Modified-Since: Fri, 02 Jul 2021 06:26:54 GMT

'''
# 需要验证的header
need_check_header = ['uuid', 'imei', 'platform', 'device-id', 'app-version', 'application-id', 'mac', 'client-id', 'brand', 'model', 'sys-ver', 'AUTHORIZATION', 'channel','wlb-imei','reg','Authorization','is-white','hardware-id','trusted-id','oaid','wlb-uid','net-env','qm-params']


headers = headers.replace('authorization','AUTHORIZATION')  # 线上有时候该字段都为小写，转化为大写处理拼接异常
headers = str_to_json(headers)

secretKey = 'd3dGiJc651gSQ8w1'  # 秘钥
sign = ''
need_check_header = sorted(need_check_header)  # 需要正序排列再加密
for key in need_check_header:
    if headers.__contains__(key):
        if key == 'Authorization':  # ios是小写需要转换成大小
            sign += '{}={}'.format(key.upper(), headers[key])  # 拼接键值对
        else:
            sign += '{}={}'.format(key, headers[key])  # 拼接键值对
sign += secretKey  # 拼接秘钥
sign = string_to_md5(sign)
print(sign)