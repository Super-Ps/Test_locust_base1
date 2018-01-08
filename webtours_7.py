#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/10/23


from locust import HttpLocust,TaskSet,task


class WebUserAction(TaskSet):
    # 初始化
    def on_start(self):
        print("--------------注意迭代开始了----------------")

    # 外层
    @task(5)
    def logget(self):
        reqbody = {
            "email": "523663197@qq.com",
            "password": "12345678"
        }
        with self.client.post("/api/club/login", reqbody, catch_response=True) as r:
            json_r = r.json()
            json_id=json_r["result"]["id"]
            if json_id == 91:
                r.success()
            else:
                r.failure("login erro:"+str(json_id))
        print("外层正在登陆....")

    # 外层内嵌
    @task(2)
    class login_user(TaskSet):
        # 内嵌循环
        @task(3)
        def get_information(self):
            self.client.get("/information/introduce")
            print('get in ...比赛介绍')

        @task(4)
        def get_process(self):
            self.client.get("/information/process")
            print('get in ...比赛流程')
        # 调用 interrupt() 跳出当前循环
        @task(2)
        def get_interrupt(self):
            print(' 调用interrupt()跳出当前类')
            self.interrupt()
    # 外层
    @task(3)
    def get_prize(self):
        self.client.get("/information/prize")
        print(' get out ...奖项设置')
    # 外层
    @task(1)
    def get_register(self):
        self.client.get("/club#/center/basic")
        print(' get out...我的俱乐部')


class WebUser(HttpLocust):
    task_set = WebUserAction
    min_wait = 3000
    max_wait = 5000
    host =  "http://test.www.makex.cc"


