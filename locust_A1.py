#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/9/20

from locust import HttpLocust, TaskSet, task

import json


#@task(2)
def index(test):
    test.client.get("/mall")

#@task(1)
def about(test):
    test.client.get("/information/introduce/")
#@task(3)
def logget(test):
    reqbody = {
        "email": "523663197@qq.com",
        "password": "12345678"
    }
    with test.client.post("/api/club/login", reqbody, catch_response=True) as r:

        json_r = r.json() #与json模块两种方式不同，方法是requests模块的 转化成json格式

        json_id=json_r["result"]["id"]

        if json_id == 91:
            r.success()
        else:
            r.failure("login erro:"+str(json_id))  #转型为字符串，因为拿到的是整型


class Websitetaks(TaskSet):
    # tasks 属性字典格式 写法等价于@task()装饰器
    tasks = {logget: 3, about: 2, index: 1}

    # tasks = [(logget,3), (about,2),(index,1)]

    # tasks = [logget,about,index]


class Websiteuser(HttpLocust):

    weight = 2

    task_set = Websitetaks
    host = "http://test.www.makex.cc"
    min_wait = 1000
    max_wait = 3000

#
# class websiteusertwo(HttpLocust):
#
#     weight = 3
#
#     task_set = Websitetaks
#
#     min_wait = 1000
#     max_wait = 2000


# 执行在dos下 在当前代码文件目录下  输入命令： locust -f 文件.py
