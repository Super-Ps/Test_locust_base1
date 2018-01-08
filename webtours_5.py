#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/10/17

from locust import HttpLocust, TaskSet, task


class UserTask(TaskSet):


    @task(2)
    class stay(TaskSet):
        @task(3)
        def readBook(self):
            self.client.get("/information/introduce")
            print('in stay....readBook')

        @task(4)
        def listenMusic(self):
            self.client.get("/information/process")
            print('in stay....listenMusic')

        @task(2)
        def logOut(self):
            print(' [※调用interrupt()]')
            self.interrupt()

    @task(5)
    def leaveed(self):
        self.client.get("/information/prize")
        print(' in  out...leave[1]')

    @task(3)
    def leave(self):
        self.client.get("/club#/register")
        print(' in  out...leave[2]')

class User(HttpLocust):

    host = "http://test.www.makex.cc"
    task_set = UserTask

    min_wait = 1000
    max_wait = 3000