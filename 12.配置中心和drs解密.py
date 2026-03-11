import requests
import json

# XQd3dgEGXXYbAgRWcxxRV3ZcTyAFIAIVAAQBCycIA3ZWc3d2

code = """


SBNVDUISRFxubUkSF0NQAVI7XgZHDREADFRTUghcBkgLBwpWHFIDX1cdXAlXCBxSVFIFBgNSVQUJAwIVRA==


"""

result = requests.post(
    url='https://key-secret-toolkit-wbddiplpzu.cn-shanghai.fcapp.run/decrypt',
    headers={
            "X-Fc-Invocation-Code-Version": "Latest",
            "X-Fc-Log-Type": "Tail",
            "content-type": "application/json"
        },
    json={
            # config_center-配置中心数据  drs-客户端离线日志  rtlrs-客户端实时日志  lrs-服务端通用日志  frontend-前端埋点日志（包括快应用，小程序）
            "app": "config_center",
            # "app": "drs",
            # "app": "ab",

            

            # test-测试环境  prod-生产环境
            "env": "prod",
            # "env": "test",

            # 项目名  具体见http://wiki.km.com/pages/viewpage.action?pageId=50598885
            # "project_name": "reader_free_ios",
            # "project_name": "abtest_server",
            "project_name": "reader_free",
            # "project_name": "listen_free",
            # "project_name": "listen_free_ios",
            # "project_name": "tap_read_android",
            # "project_name": "tap_read_ios",
            # "project_name": "reader_fast_panda",
            # "project_name": "reader_writer_assistant_ios",
            # "project_name": "reader_fast_eggplant",
            # "project_name": "reader_free_harmony",
            # 加密数据
            # "data": "HhJaDlxeWlVKR1tqHhBdWwcUXVVAWRs2QEgXEAcXEV4KXhtbEAkFCg9VVQBSBAYBWlQTHEAXQBIHRg9XTkcDWwkSAxoQXFJGWEdbEx5uEngCFF9TCj8bWBk4FzUVDBZUDWwbW0lkEVBIET0TX24SQBEUVGxAT2VAARdfOkBfPhURQkwEbhofbhsOEm1HCGwWFxNEVT5BRE4+RkUJEhASa0cKQj0QTFZXVwQGVBduEg4/Q0psPj8bFgsQWQM+OT4VX2xlPRDRrqDc1fDU3IbViNqGm6c+P2VATjhpOkAIEVA5bGVDCGRvbhuA3YiCmKfR5eTUnts/ZT5ASGk6PkcBWBBeTT1uZBEICFUcbUdPTRg/Q1NDPkEDGT5GVwkbOUANHmwbA11XWEFlR1ttRwMBBVJNAxxRPxsfTjgXAQsXDmtHCkI9EFpcXVIWPRNfbhIFUk0DAk5QCk5XUQA6QBgfSkccGwJaXVBZShAME18QCQFUVQgJU1cbHx85GUQWFwNUAG9QBRACEVddAFUBUFAIGVsFUgdPVwEBUEkNAlRdTwVRCVxWU1lSAghTUxMY"
            "data": code
}
).json()
print(result)
print('='*50+'data数据解密'+'='*50)
python_data = json.loads(result['data'])
print(json.dumps(python_data, indent=4))

print('='*50+'返回配置中心的数据列表'+'='*50)
# print(python_data['configs'][0]['all']['data'])
# print(json.dumps(python_data['configs'][0]['all']['data'], indent=4))
# for i in python_data['configs']:
    # print(json.dumps(i, indent=4))