import requests
import urllib3

# 隐藏IP异常报错
urllib3.disable_warnings()

# a= requests.get(url='https://data.zhai78.com/openOneBad.php', verify=False).json()['txt']
# print(a)

import re

str1 = 'import "aa/bb.proto"import "aa/bb.proto34"1'
res = re.findall(r'"([^"]*)"', str1)
print(res)

print(__file__)
print(__name__)

from selectolax.parser import HTMLParser
f = open('/Users/admin/PycharmProject/qaarm-freebook-agilityteam001-test/reports/pytest_report/report.html', "rb")
html = f.read()
text = HTMLParser(html).text(strip=True)
print(text)
result = re.search('check the boxes to filter the results.(.*)Results', text)
print(result.group(1))

# import ctypes
# ctypes.windll.user32.mouse_event(MOUSEEVENTF_ABSOLUTE|MOUSEEVENTF_MOVE, 100, 200, 0, 0)

import json

data = "{\"aggs\":[{\"count\":\"3\",\"eventid\":\"reader_chapcomment_#_show\",\"sid\":\"1668657995973\",\"version\":\"7.9\"},{\"count\":\"3\",\"eventid\":\"reader_chapcomment_withcontent_show\",\"sid\":\"1668657995973\",\"version\":\"7.9\"},{\"count\":\"3\",\"eventid\":\"reader_chapterend_ticket_show\",\"sid\":\"1668657995973\",\"version\":\"7.9\"},{\"count\":\"3\",\"eventid\":\"reader_chapterend_reward_show\",\"sid\":\"1668657995973\",\"version\":\"7.9\"},{\"count\":\"3\",\"eventid\":\"reader_textlink_#_show\",\"params\":{\"page\":\"5\",\"statid\":\"awardcoin\"},\"sid\":\"1668657995973\",\"version\":\"7.9\"},{\"count\":\"1\",\"eventid\":\"listen_#_#_move\",\"params\":{\"bookid\":\"156500\",\"chapterid\":\"16656279892376\",\"sortid\":\"2376\"},\"sid\":\"1668657995973\",\"version\":\"7.9\"},{\"count\":\"1\",\"eventid\":\"listen_time_#_use\",\"params\":{\"bookid\":\"156500\",\"chapterid\":\"16656279892376\",\"duration\":\"55975\",\"sortid\":\"2376\",\"voicetype\":\"tts\"},\"sid\":\"1668657995973\",\"version\":\"7.9\"},{\"count\":\"6\",\"eventid\":\"reader_#_awardcoin_show\",\"sid\":\"1668657995973\",\"version\":\"7.9\"},{\"count\":\"1\",\"eventid\":\"listen_time_#_use\",\"params\":{\"bookid\":\"156500\",\"chapterid\":\"16656279892377\",\"duration\":\"182535\",\"sortid\":\"2377\",\"voicetype\":\"tts\"},\"sid\":\"1668657995973\",\"version\":\"7.9\"},{\"count\":\"1\",\"eventid\":\"listen_#_#_move\",\"params\":{\"bookid\":\"156500\",\"chapterid\":\"16656279892377\",\"sortid\":\"2377\"},\"sid\":\"1668657995973\",\"version\":\"7.9\"},{\"count\":\"1\",\"eventid\":\"listen_time_#_use\",\"params\":{\"bookid\":\"156500\",\"chapterid\":\"16656279892377\",\"duration\":\"67759\",\"sortid\":\"2377\",\"voicetype\":\"tts\"},\"sid\":\"1668657995973\",\"version\":\"7.9\"},{\"count\":\"1\",\"eventid\":\"listen_time_#_use\",\"params\":{\"bookid\":\"156500\",\"chapterid\":\"16657278062378\",\"duration\":\"181315\",\"sortid\":\"2378\",\"voicetype\":\"tts\"},\"sid\":\"1668657995973\",\"version\":\"7.9\"},{\"count\":\"1\",\"eventid\":\"listen_#_#_move\",\"params\":{\"bookid\":\"156500\",\"chapterid\":\"16657278062378\",\"sortid\":\"2378\"},\"sid\":\"1668657995973\",\"version\":\"7.9\"},{\"count\":\"1\",\"eventid\":\"listen_time_#_use\",\"params\":{\"bookid\":\"156500\",\"chapterid\":\"16657278062378\",\"duration\":\"64198\",\"sortid\":\"2378\",\"voicetype\":\"tts\"},\"sid\":\"1668657995973\",\"version\":\"7.9\"},{\"count\":\"1\",\"eventid\":\"listen_time_#_use\",\"params\":{\"bookid\":\"156500\",\"chapterid\":\"16657278062379\",\"duration\":\"186558\",\"sortid\":\"2379\",\"voicetype\":\"tts\"},\"sid\":\"1668657995973\",\"version\":\"7.9\"}],\"devs\":[],\"environment\":{\"access\":\"WiFi\",\"appversion\":\"7.9\",\"battery\":34,\"brand\":\"Apple\",\"channel\":\"qi-appstore_wm\",\"crackeddevice\":\"0\",\"devicemodel\":\"iPhone14,5\",\"firstlaunch\":1644111078537,\"imsi\":\"unknown\",\"logintype\":9,\"os\":\"iOS\",\"osversion\":\"16.0\",\"packageinstalltime\":1644101340906,\"packagename\":\"com.yueyou.cyreader\",\"projectname\":\"reader_free_ios\",\"resolution\":\"1170*2532\",\"sdkua\":\"16_0\",\"sdkversion\":\"2.0.5\",\"versioncode\":\"7090020\"},\"events\":[],\"identity\":{\"accountid\":\"146868966\",\"idfa\":\"F39BD4E1-069D-4806-8908-BA71E657ACF4\",\"idfv\":\"9D2536C8-0689-4DE2-ABB3-EB4553A3D7D3\",\"keychainidfa\":\"\",\"preusecret\":\"a6b660d9dbb715e477c12726e04bcbed\",\"preusecretversion\":\"20211207\",\"trustedid\":\"D20iGI8oKeP53uay1MoXzT3cOSxOcJQe2Jzy9vH7McrzEXb7\",\"trustedidfa\":\"F39BD4E1-069D-4806-8908-BA71E657ACF4\",\"uid\":\"#CDF8DBEF-7673-4012-B915-9C4B0F0AF493\",\"usecret\":\"f229faa5fa10bd3324bb67ea85b16b6b\",\"usecretversion\":\"20220111\"},\"ip\":\"183.141.20.129\",\"launchs\":[],\"ts\":1668660777}"
js_data = json.loads(data)
print(json.dumps(js_data, indent=4))

event_detail_data ='deeply nested 好的'
event = {}
message = {}
event['details'] = event_detail_data
message['data'] = event
print(message)
json_to_send = json.dumps(message)
print(json_to_send)

# import zlib and crc32
import zlib

s = b'{\"Launch\":{\"Switch\":{\"bqt\":\"true\",\"csj\":\"true\",\"ks\":\"true\"},\"popup\":{\"teenager\":\"{\\\"title\\\":\\\"\u9752\u5c11\u5e74\u5f39\u7a97\\\",\\\"msg\\\":\\\"\u5f39\u7a97\u5185\u5bb9\\\",\\\"count\\\":10}\"}},\"bs\":{\"boy\":{\"books\":\"1111,2,3\"},\"girl\":{\"books\":\"11,22,33,555\"}}}'
# using zlib.crc32() method
t = zlib.crc32(s)
print(t)