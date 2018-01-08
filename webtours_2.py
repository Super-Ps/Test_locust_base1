#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/10/13

from locust import HttpLocust, TaskSet, task

# 循环取数据，数据可重复使用
class OwebAction(TaskSet):

    def on_start(self):

        self.index = 0
    @task
    def user_url(self):
        # 下标+1,除列表长度 拿余数作为下一次列表下标
       self.index = (self.index+1) % len(self.locust.url_data)
       print('self.index :%s' %self.index )
       url = self.locust.url_data[self.index]
       print('获取url：%s' % url)
       self.client.get(url)

class OwebUser(HttpLocust):

    weight = 2

    host = 'http://test.www.makex.cc'
    task_set = OwebAction
    url_data = ['/information/introduce', '/information/rule', '/information/process',
                '/information/prize', '/club#/register']
    min_wait = 1000
    max_wait = 3000


class OwebUser(HttpLocust):
    weight = 4

    host = 'http://test.www.makex.cc'
    task_set = OwebAction
    url_data = ['/information/introduce', '/information/rule', '/information/process',
                '/information/prize', '/club#/register']
    min_wait = 1000
    max_wait = 2000