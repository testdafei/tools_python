import grequests
import urllib3
import time
from hashlib import md5

# 隐藏IP异常报错
urllib3.disable_warnings()
headers = {
    'Host': 'update.wtzw.com',
    'accept-encoding': 'gzip',
    'content-type': 'application/x-www-form-urlencoded'
}


def eas_config(num):
    eas_sign = generate_eas_sign(json)
    json.update({'eas_sign': eas_sign})
    req_list = [ # 请求列表
    grequests.post(
            url='https://update.wtzw.com/eas-config',
            headers=headers,
            data=json,
            verify=False
    ) for i in range(num)
    ]
    num_memory = 0
    num_hprof = 0
    fail_res = 0
    start = time.time()
    res_list = grequests.map(req_list) # 并行发送，等最后一个运行完后返回
    end = time.time()
    for i in res_list:
        if i:
            i = i.json()
        else:
            print('返回为', i)
            fail_res = fail_res + 1
            continue
        print(i)
        memory = i['data']['memory_status']
        hprof = i['data']['hprof_status']
        num_memory = num_memory + int(memory)
        num_hprof = num_hprof + int(hprof)
    print('{}个请求并发，内存采样率{}%,用时{}秒，失败{}个'.format(num, num_memory*100/num, end-start, fail_res))
    print('{}个请求并发，堆转储采样率{}%,用时{}秒'.format(num, num_hprof*100/num, end-start))


def generate_eas_sign(bodys):
    """
    生成加密字段update_sign
    :param bodys:
    :return:
    """
    # 需要验证的body
    need_check_body = ['channel', 'version_code', 'os_version', 'brand',  'device_model',  'project', 'package_name',
                       'ts', 'account_id', 'secret_key']
    # secretKey = {'secret_key': 'f5zoy7m8ru174t56z9efrt8u5xq6ewrn'}  # ios秘钥
    # secretKey = {'secret_key': 'e7pf1zhmloyzxiqbvxyrvka5bqa4alum'}  # android秘钥
    if bodys['project'] == 'reader_free':
        secretKey = {'secret_key': 'e7pf1zhmloyzxiqbvxyrvka5bqa4alum'}
    else:
        secretKey = {'secret_key': 'f5zoy7m8ru174t56z9efrt8u5xq6ewrn'}
    bodys.update(secretKey)
    update_sign = ''
    need_check_body = sorted(need_check_body)  # 需要正序排列再加密
    for key in need_check_body:
        if bodys.__contains__(key):
            update_sign += '{}={}'.format(key, bodys[key])  # 拼接键值对
    update_sign = string_to_md5(str(update_sign))  # md5加密
    return update_sign


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

json = {
    'account_id': '301269617',
    'device_model': 'SPN-AL00',
    # 'device_model': 'A',
    'eas_sign': '38afd98cfef7bc39f63219ddeb2c0098',
    'os_version': '10.0',
    'channel': 'unknown',
    'version_code': '61900',
    'package_name': 'com.kmxs.reader',
    # 'project': 'reader_free_ios',
    'project': 'reader_free',
    'brand': 'HUAWEI',
    'ts': '1652517382'
}
eas_config(500)