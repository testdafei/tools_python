import requests


def translate(data_i):
    data = {'doctype': 'json', 'type': 'ZH_CN2EN', 'i': data_i}
    r = requests.get("http://fanyi.youdao.com/translate", params=data)
    result = r.json()
    result = list(result['translateResult'][0][0].values())
    # print(result)
    return result


def generate(s):
    s = s.title().replace(' ', '').replace('\n', '').replace('\r', '')
    s = s + 'Text'
    return s[0].lower()+s[1:]


input = '''

立即抽奖
看视频抽奖

    '''

model = '''
    def click{}(self):
        \'\'\'幸运大转盘页面\'\'\'
        with allure.step('幸运大转盘页面，点击{}'):
            self.clickElement(self.{})
'''
list_date = []
data = input.strip().split('\n')
# print(data)
for i in data:
    res = translate(i)
    res[1] = generate(res[1])
    key_start = res[1][:-4]
    key_end = res[1][-4:].lower()
    print('self.{} = self.poco({}=self.{})'.format(key_start, key_end, res[1]))
    list_date.append(res)
print(list_date)
for i in list_date:
    print("{} = '{}'".format(i[1], i[0]))

for i in list_date:
    i_end = i[1][-4:]
    i_start = i[1][:-4]
    i_start_A = i_start[0].upper()+i_start[1:]
    if i_end == 'Text':
        name = i[0]
    else:
        name = ''
    print(model.format(i_start_A, name, i_start), end='')

print('======'*20)

input = '''

    closeName = 'javascript:void(0)' 
    '''

model = '''
    def click{}(self):
        \'\'\'我的金币页面\'\'\'
        with allure.step('我的金币页面，点击{}'):
            self.clickElement(self.{})
'''
list_date = []
data = input.strip().split('\n')
# print(data)

for i in data:
    list = i.split('=')
    key = list[0].strip()
    value = list[1].strip().replace("\'", "")
    tup = (key, value)
    list_date.append(tup)

    key_end = key[-4:].lower()
    key_start = key[:-4]

    print('self.{} = self.poco({}=self.{})'.format(key_start, key_end, key))
print(list_date)

for i in list_date:
    i_end = i[0][-4:]
    i_start = i[0][:-4]
    i_start_A = i_start[0].upper()+i_start[1:]
    if i_end == 'Text':
        name = i[0]
    else:
        name = ''
    print(model.format(i_start_A, name, i_start), end='')
