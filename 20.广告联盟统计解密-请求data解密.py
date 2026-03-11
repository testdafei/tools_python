import requests
import json

# XQd3dgEGXXYbAgRWcxxRV3ZcTyAFIAIVAAQBCycIA3ZWc3d2

code = """

GEZSExJtD1VDAkFbUxIaE1wDTFIRWURzXSJ/biR2NGxSImsxCWADYTVPNTM3WG5wbTtsd2QtLXF0KmZoDWkpfgQIdysJaAV0DQkGNjYBVXBTOFtiAgQubHAEA2sKZgBsNV1RJTNaPnInSCA1M2ZUcgkBD3QBWipiBTpieiR6J382IlAxBXwEYzZQLjMJclR2UDN/ZlgXAmReOm5+VwQCeDJQdiEOZDVkUHkvNyAIc2RQAVx1ZSUAZlIyYmgnZgVqGxRRJiRjBHYzaTAxN35+c08JbmJELj9zBSpmawpADG0mDHAhJ38rYwZ9AjA0AGd3CSN5dFQMBHVCKWdvV2Y7fTUXciFTcyRwI202J1Fhc3QIN3ZrdToHY00hYn9XRy18CDZFJDdjJ3AZXCgzMH5EfkAJbGtfGzNsdzZ/aA4AMXgIKnc2FXALd1BcJTFQdmd+aidocWEXPHd0D2F4J30reCIxdTUOcyRnMH0hIyd5dWR6NH9kZVYCZXMMZngiWyphNiF3Jg4LNGc3dSwgDXVzcH4reXJiCCp2BAdxfzNqO2w1JmQlU0ohZFB6ACMNWGFwTy9bZXJaM2IFG2BsEWkkfzULcCEVZzNwBgwhNQ1Tc2duK3lkciIlc00bc24KcgZhJFFQJwgHMHM3ejI6NH1/Y18abmtlJT9icyFnajdmNGEiPWYhI3w+cyNIAjcGU3dlfiBrcl8XAmF0JWVhVwAhbDEXViUafyhwCnUnMzBHdHAJMGlmZVMufEIpYWwRdQZ9JVR3IVJeBHMWCTEkJ2FyZ08BfGZyEzBsQg9QbyR+KH8hKmsnGlYAdw1ANDQwYlV0ehZdYkspP2FjOnJ/HmYneFMiRjQxcAV0GUsCNydpHXRUK2hRdRc+dmMHcXhWaSl4Ig9wISR8M2MkCAEjDQFAd24kWVJ2VjNldyp/bjdfMXgLFGIrJGM+ZzNhJSEzcWxjeTdvdmQ6LWxnKVV/EVclfgtUYiIgdCF+UW4HMQl6VHIJBn9yWyopfHRSYmsNQCduFC59MSN8LmIjbSAhIHZ4YAkremFlJQR2clNxahFmNG8hF3olGwYUeiINETMzZWVwVCBwa18XM1ZkKmRoVmkpfg8PZztTeyhiNAwqNSNxbGN5I3x1AiInbHJbem4KZjBvISl6MhtGUH0jDVYGDXV1Y1A0f2t1NTZjBDpydh5hLG8mIXcmCwcnZCZ6BzUjAF19cAlPVl0HVGBbW3BhAQEBYzsmRyJSWjBiJ30BNhlEYXUIBntiAQcCYU0yZm83RzF4BAhkISRRLWQGTyojIGV3Z1QGc2ICIjJgQjFzfR59IHghXHQ0JwojZyBtNCE3eXFjUDR/ZQMuBHd3AFh6AXk3bwQUVyYJXT5pCmoNMFBTYnRUWnRrYQwlZUItYX5WVwJoJQxhOwVRInAbDTImNEBzcwkOXFJ2Gz9sQjFyfSBlJn0EEGAhJHMoZAZ5ICEgYWxjejNwcl8qJWxZNgNuV3ICYTEpejIVeDxyMwk3NDNcdGJTEXpkZTEFZXcHfWsOYSZqBBxlMTB4BWkNUwIhGXJnZGlXbXRiDC1jZBdxfzNqL28lLkcyI1YhaSR2WiMNZnF1CVZdcWE6J3xzJXRxD1gCbwhUaSA3YBVpGVAbNFBqfnJpUntiYgs0dV0iRVw+WwJcO1xwNjd0VnQ3SDY6JAUAegsBSlJdE1dRXQRYcgpqMXwmIWUmCnguZCdqNwAKaW90bix/cGETB3VzJmZhJ0AAayYQZzUFAyFiCnYzIApEcnUJEl5SdRcDYlIxcn0jaSZ4IlVhIgloI3YwBV5ATRJFWF8MGgkRAlRQDAcOCV8CVl8HAlJaAQtWV1QJVFpQAldQDgYLCwtBGw==


"""


result = requests.post(
    url='https://key-secret-toolkit-wbddiplpzu.cn-shanghai.fcapp.run/ad-drs/decrypt',
    headers={
            "X-Fc-Invocation-Code-Version": "Latest",
            "X-Fc-Log-Type": "Tail",
            "content-type": "application/json"
        },
    json={
             "data": code,
            "app_name": "prod_app_android",
            # "app_name": "prod_app_ios",
            "env": "prod_app",


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