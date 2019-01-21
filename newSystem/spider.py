# -*- coding: utf-8 -*-

from django.http import HttpResponse
import requests
import time
import json
import sys
from pyquery import PyQuery as pq

class Loginer():

    def __init__(self):
        self.session = requests.session()

    def getPublicKey(self):
        url1 = 'http://zf.ahu.cn/'
        url2 = 'http://zf.ahu.cn/IdentityServer/Account/getPublicKey'

        res1 = self.session.get(url1)
        doc = pq(res1.text)
        __RequestVerificationToken = doc(
            'body > div > div.login-div > div.col-md-4.form > form > input[type="hidden"]:nth-child(5)').attr("value")
        self.RequestVerificationToken = __RequestVerificationToken
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
        res2 = self.session.post(url2, headers=headers)
        _response_json = res2.json()
        response_json = json.dumps(_response_json)
        return response_json

    def reflushToken(self):
        print('RequestVerificationToken1:', self.RequestVerificationToken)
        reflushTokenUrl = 'http://zf.ahu.cn/IdentityServer/Account/gslogin'
        res3 = self.session.get(reflushTokenUrl)
        doc1 = pq(res3.text)
        __RequestVerificationToken = doc1(
            'body > div > div.login-div > div.col-md-4.form > form > input[type="hidden"]:nth-child(5)').attr("value")
        self.RequestVerificationToken = __RequestVerificationToken
        print('RequestVerificationToken2:', self.RequestVerificationToken)


    def post_data(self, username, password):
        # try:
        postDataToLoginUrl = 'http://zf.ahu.cn/IdentityServer/Account/Login'
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Content-Length': '478',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'zf.ahu.cn',
            'Origin': 'null',
            'Proxy-Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }
        self.header = header
        data = {
            'ReturnUrl': '',
            'username': username,
            '__RequestVerificationToken': self.RequestVerificationToken,
            'password': password
        }
        # print(data)
        postDataToLoginUrl_respose = self.session.post(postDataToLoginUrl, headers=header, data=data)
        # print(postDataToLoginUrl_respose.status_code)
        # print(postDataToLoginUrl_respose.text)
        with open('test.html', 'wb') as f:
            f.write(postDataToLoginUrl_respose.content)




class Grades(Loginer):

    def __init__(self):
        super().__init__()


    def post_gradedata(self):
        getGradeUrl = 'http://zf.ahu.cn/cjgl/Student/CJCX/KCCJCX'
        getGrade_response = self.session.get(getGradeUrl)
        print(getGrade_response.status_code)
        with open('test1.html', 'wb') as f:
            f.write(getGrade_response.content)
        getGradeDetailUrl = 'http://zf.ahu.cn/Cjgl/student/CJCX/KCXXXX'
        self.reflushToken()
        headers = {
            '__RequestVerificationToken': self.RequestVerificationToken,
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '101',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Host': 'zf.ahu.cn',
            'Referer': 'http://zf.ahu.cn/Cjgl/Student/CJCX/KCCJCX',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        data = {
            'send_by_bootstrap_table': 'true',
            'XN': '2018-2019',
            'XQ': '1',
            'sortName': 'XKKH',
            'sortOrder': 'asc',
            'showCount': '30',
            'currentPage': '1',
        }
        getGradeDetail_response = self.session.post(getGradeDetailUrl, data=data, headers=headers)
        print(getGradeDetail_response.status_code)
        with open('test2.html', 'wb') as f:
            f.write(getGradeDetail_response.content)




