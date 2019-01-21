# -*- coding: utf-8 -*-

from django.http import HttpResponse
import requests
import time
import json
import sys
from pyquery import PyQuery as pq

class Loginer():

    def __init__(self):
        # self.user = str(user)
        # self.passwd = str(passwd)
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


    def post_data(self, username, password):
        # try:
        url = 'http://zf.ahu.cn/IdentityServer/Account/Login'
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
        print(data)
        respose = self.session.post(url, headers=header, data=data)
        print(respose.status_code)
        print(respose.text)
        print(111111)
        # self.cookie = self.req.request.headers['cookie']
        ppot = r'用户名或密码不正确'




class Grades(Loginer):

    def __init__(self):
        super().__init__()
        # self.year = year
        # self.term = term
        # self.url1 = 'http://202.119.206.62/jwglxt/cjcx/cjcx_cxDgXscj.html?gnmkdm=N305005&layout=default&su=' + user
        # self.url2 = 'http://202.119.206.62/jwglxt/cjcx/cjcx_cxDgXscj.html?doType=query&gnmkdm=N305005'

    # def welcome(self):
    #     try:
    #         stu_name = self.req_2['items'][0]['xm']
    #         sch_stu = self.req_2['items'][0]['xslb']
    #         institute = self.req_2['items'][0]['jgmc']
    #         classss = self.req_2['items'][0]['bj']
    #         print('')
    #         print('')
    #         print(stu_name + '同学,欢迎您!!!')
    #         print('')
    #         print('姓名:{}\t学历:{}\t\t学院:{}\t班级:{}'.format(stu_name, sch_stu, institute, classss))
    #         print('')
    #         time.sleep(1)
    #     except:
    #         print('无当前学期,请重试')

    # def post_gradedata(self):
    #     try:
    #         data = {'_search': 'false',
    #                 'nd': int(time.time()),
    #                 'queryModel.currentPage': '1',
    #                 'queryModel.showCount': '15',
    #                 'queryModel.sortName': '',
    #                 'queryModel.sortOrder': 'asc',
    #                 'time': '0',
    #                 'xnm': self.year,
    #                 'xqm': self.term
    #                 }
    #         req_1 = self.sessions.post(self.url1, data=data, headers=self.header)
    #         req_2 = self.sessions.post(self.url2, data=data, headers=self.header)
    #         self.req_2 = req_2.json()
    #     except:
    #         print('获取失败,请重试...')
    #         sys.exit()

    # def print_geades(self):
    #     try:
    #         plt = '{0:{4}<15}\t{1:{4}<6}\t{2:{4}<6}\t{3:{4}<4}'
    #         gk = 0
    #         zkm = 0
    #         print('')
    #         print('--------------------------------------------------------------------------------')
    #         print(plt.format('课程', '成绩', '绩点', '教师', chr(12288)))
    #         print('--------------------------------------------------------------------------------')
    #         for i in self.req_2['items']:
    #             print(plt.format(i['kcmc'], i['bfzcj'], i['jd'], i['jsxm'], chr(12288)))
    #             if i['bfzcj'] < 60:
    #                 gk += 1
    #             zkm += 1
    #         print('--------------------------------------------------------------------------------')
    #         print('')
    #         print('通过科目数:{}{}'.format(zkm - gk, '门'))
    #         print('挂科科目数:' + str(gk) + '门')
    #         print('')
    #         print('')
    #     except:
    #         print('无当前学期,请重试')


# if __name__ == '__main__':
#     user = 'E31614002'
#     passwd = 'wang921207'
#     myGrade = Grades(user, passwd)
#     myGrade.getPublicKey()
#     myGrade.post_data()



