#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/10/10






from lxml import etree
from locust import HttpLocust
from locust import TaskSet
from locust import task
import json


class WebAction(TaskSet):



    def on_strar(self):
        re_body = {
            "email": "523663197@qq.com",
            "password": "12345678"
        }
        with self.client.post("/api/club/login", re_body, catch_response=True) as r_sponse:
            r_sponse_json = r_sponse.json()
            msg=r_sponse_json["result"]["status"]
            if msg =="normal1":
                r_sponse.success()
            else:
                r_sponse.failure(" login error "+msg)
    #
    # @task(2)
    # def user_login(self):
    #     re_body = {
    #         "email": "523663197@qq.com",
    #         "password": "12345678"
    #     }
    #     with self.client.post("/api/club/login", re_body, catch_response=True) as r_sponse:
    #         r_sponse_json = r_sponse.json()
    #         msg=r_sponse_json["result"]["status"]
    #         if msg =="normal1":
    #             r_sponse.success()
    #         else:
    #             r_sponse.failure(" login error "+msg)

    @task(1)
    def index(self):
        self.client.get("/mall")



class WebUser(HttpLocust):
    weight = 2

    host = "http://test.www.makex.cc"

    task_set = WebAction

    min_wait = 200
    max_wait = 500



