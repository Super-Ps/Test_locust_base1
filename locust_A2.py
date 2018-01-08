#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/9/25

from lxml import etree

from locust import HttpLocust, TaskSet,task

import json




#http://127.0.0.1:1080/WebTours/



class WebActhion(TaskSet):

    @staticmethod
    def get_session(html):

        tree = etree.HTML(html.decode("utf-8"))
        tree_a=tree.xpath("//frame ")
        for x in tree_a:
            x_text=x.text
            print(x_text)
            x_attrib=x.attrib
            print(x_attrib)

            #return x_text , x_attrib

    @task(4)
    def test_login(self):
        html = self.client.get("/information/introduce").content

        re_html = self.get_session(html)

        print(re_html)


    def on_strar(self):
        pass


    # @task(2)
    # def process_page(self):
    #     self.client.get("/information/process")
    #
    #
    # @task(3)
    # def about(self):
    #     self.client.get("/information/introduce/")
    #
    #
    # @task(4)
    # def index(self):
    #     self.client.get("/mall")


    @task(5)
    def login_user(self):
        reqbody = {
            "email": "523663197@qq.com",
            "password": "12345678"
                }
        with self.client.post("/api/club/login", reqbody, catch_response=True) as r:
            r_json = r.json()
            msg = r_json["result"]["status"]
            if msg == "normal":
                r.success()
                #print(r.success())
            else:
                r.failure("login error "+msg)




class Webuser(HttpLocust):

    weight = 2

    host = "http://127.0.0.1:1080/WebTours/"

    task_set = WebActhion

    min_wait =500

    max_wait =1000

    # 登陆返回
    '''
    {
    "code": 1,
    "msg": "登陆成功",
    "result": {
        "id": 91,
        "email": "523663197@qq.com",
        "actived": "activated",
        "status": "normal"
                }
    }
    '''
class Webusertwo(HttpLocust):

    weight = 3

    host = "http://test.www.makex.cc"

    task_set = WebActhion

    min_wait =500

    max_wait =1000