import json

import requests
from pyquery import PyQuery as pq

url1 = 'http://zf.ahu.cn/'
url2 = 'http://zf.ahu.cn/IdentityServer/Account/getPublicKey'
session = requests.session()
res1 = session.get(url1)
doc = pq(res1.text)
__RequestVerificationToken = doc(
    'body > div > div.login-div > div.col-md-4.form > form > input[type="hidden"]:nth-child(5)').attr("value")
print(__RequestVerificationToken)
headers = {
    '__RequestVerificationToken': __RequestVerificationToken,
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Length': '0',
    'Host': 'zf.ahu.cn',
    'Origin': 'http://zf.ahu.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Proxy-Connection': 'keep-alive',
}
res2 = session.post(url2, headers=headers)
x = res2.json()
# print(x)
# print(type(x))
y = json.dumps(x)
# print(y)
# print(type(y))
print(y)
