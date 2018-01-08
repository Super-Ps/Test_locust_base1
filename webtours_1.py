#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/10/12


from locust import HttpLocust,TaskSet ,task
from lxml import etree
import re

import  pymysql


 # 通过 lxml类处理关联， 也可以采用re.search
class WebUserAction(TaskSet):

    def on_start(self):
        pass
    @task(2)
    # 注册请求
    def user_pl(self):

        data = {'username': 'jonny4301',
                'password': 'jy123456',
                'passwordConfirm': 'jy123456',
                'firstName': 'jonny3',
                'lastName': 'ps3',
                'address1': 'Street + Address + no10003',
                'address2': 'CityStateZipno10003',
                'register.x': '52',
                'register.y': '8'
                }

        with self.client.post("/login.pl", data, catch_response=True) as r_response:
            html_text = r_response.text
            # html解析
            r_html = etree.HTML(html_text)
            #print('返回html对象：', r_html)
            # xpath方法定位截取
            r_text = r_html.xpath("//blockquote")
            # 取列表元素,调用 ResponseContextManager类方法判断
            for x in r_text:
                r_x = x.text
                #print('获取元素b：', r_x, end='')
                if r_x == 'Thank you,':
                    r_response.success()
                else:
                    r_response.failure(" failure")



class Webclient(HttpLocust):

    pymysql.connect

    task_set = WebUserAction
    host = "http://127.0.0.1:1080/WebTours/"
    min_wait = 5000
    max_wait = 5000