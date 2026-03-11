raw_headers = '''
net-env: 1
reg: 
channel: unknown
is-white: 
platform: android
application-id: com.kmxs.reader
authorization: 
app-version: 77500
qm-params: cLG5Ozo7paHWH-x8h-J3H5w54l45A5HwH5w54ln1pqYMtq2-HTZ5Aqk-pI4E4lRxpyFLghNzp3HjHzk2uz2Tp3U1paHWHTHwgTfwNTHegh4nNhFlpTFY4e9npzkTgzfEghp2NIOrgy0eNek54e2-4e9LNyHwgIFUgIk-gzR54hoTgq0lH5w5mqU2m3HWH5HjHzUx4LHWH5HjHzUDpyRjHTZ53-nHtfoAgI95taGD4q2-HTZ5Nho24qozph4Q4eu2p3MMpqHUtqGTNq0QpT4n4lfngepzAh2xH5w5Blo1paU7BLUT4qNZp3HWHTfnpqoxpzfltqgEpqfQNyR5N3U54eRxtq4lgqN2ghglpT-Y43HjHSsZBlY2tqn2uzRjHTZ53aHjHSN2OEN1BlrQmqF5A5HnNefwNT4lNIOnAI9rH5w5OlJUOzN2uq2-HTZ5pI-Yge4YAh-QNhx545MMgIu2thKENT0QNIu-Ay0YNyHeAI0YH5w5OEkxuy2TCENTBEG2HTZ5garrH5w5OE2etCp2O5HWHT0LH5w5uCR1paHWHT9wgI9wgI9wth9w4e9QNe4wgaMwgI9wth9wgI9wgI9wgI9wgaHjHSuj45U1BqR1HTZ5H5w5uln5tCR1paHWHTfnpqoxpzfltqgEpqfQNyR5N3U54eRxtq4lgqN2ghglpT-Y43GJ
sign: 8d99d8dbaa6c7ffac2bf0d392e51376d
no-permiss: 3
user-agent: webviewversion/0
content-type: application/x-www-form-urlencoded
content-length: 254
accept-encoding: gzip

'''
raw_body = 'account_id=301269617&device_model=SPN-AL00&eas_sign=38afd98cfef7bc39f63219ddeb2c0098&os_version=10&channel=unknown&version_code=61900&package_name=com.kmxs.reader&project=reader_free&brand=HUAWEI&ts=1652517382'

# format1/key='value',      format2/key=None,     format3/'key': key,     format4/key=key,


def generate_format1_from_raw_headers(raw_headers):
    # data = raw_headers.strip().split('\n')
    list_date = ["{}='{}'".format(i.split(':')[0].strip(), i.split(':')[1].strip()) for i in raw_headers.strip().split('\n')]
    # for i in data:
    #     list = i.split(':')
    #     key= list[0].strip()
    #     value = list[1].strip()
    #     # print("{}='{}'".format(key, value))
    #     list_date.append("{}='{}'".format(key, value))
    str_data = ',\n'.join(list_date)
    print(str_data)


def generate_format1_from_raw_body(raw_body):
    data = raw_body.strip().split('&')
    list_date = []
    for i in data:
        list = i.split('=')
        key= list[0].strip()
        value = list[1].strip()
        list_date.append("{}='{}'".format(key, value))
    str_data = ',\n'.join(list_date)
    print(str_data)


def generate_format2_from_raw_headers(raw_headers):
    data = raw_headers.strip().split('\n')
    list_date = []
    for i in data:
        list = i.split(':')
        key= list[0].strip()
        list_date.append("{}=None".format(key))
    str_data = ', '.join(list_date)
    print(str_data)

def generate_format2_from_raw_body(raw_body):
    data = raw_body.strip().split('&')
    list_date = []
    for i in data:
        list = i.split('=')
        key= list[0].strip()
        list_date.append("{}=None".format(key))
    str_data = ', '.join(list_date)
    print(str_data)


def generate_format3_from_raw_headers(raw_headers):
    list_date = ["'{0}': {0}".format(i.split(':')[0].strip()) for i in raw_headers.strip().split('\n')]
    str_data = ',\n'.join(list_date)
    print(str_data)


def generate_format3_from_raw_body(raw_body):
    list_date = ["'{0}': {0}".format(i.split('=')[0].strip()) for i in raw_body.strip().split('&')]
    str_data = ',\n'.join(list_date)
    print(str_data)


def generate_format4_from_raw_headers(raw_headers):
    data = raw_headers.strip().split('\n')
    list_date = []
    for i in data:
        list = i.split(':')
        key= list[0].strip()
        list_date.append("{0}={0}".format(key))
    str_data = ', '.join(list_date)
    print(str_data)


def generate_format4_from_raw_body(raw_body):
    data = raw_body.strip().split('&')
    list_date = []
    for i in data:
        list = i.split('=')
        key= list[0].strip()
        list_date.append("{0}={0}".format(key))
    str_data = ', '.join(list_date)
    print(str_data)


generate_format1_from_raw_headers(raw_headers)
print('*'*100)
generate_format1_from_raw_body(raw_body)
print('*'*100)
generate_format2_from_raw_headers(raw_headers)
print('*'*100)
generate_format2_from_raw_body(raw_body)
print('*'*100)
generate_format3_from_raw_headers(raw_headers)
print('*'*100)
generate_format3_from_raw_body(raw_body)
print('*'*100)
generate_format4_from_raw_headers(raw_headers)
print('*'*100)
generate_format4_from_raw_body(raw_body)