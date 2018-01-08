#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/10/16

from locust import TaskSet, task, HttpLocust
import queue
class UserBehavior(TaskSet):
    @task
    def test_register(self):
        try:
            data = self.locust.user_data_queue.get()
        except queue.Empty:
            print('account data run out, test ended.')
            exit(0)
        print('register with user: {}, pwd: {}'.format(data['username'], data['password']))
        payload = {
            'username': data['username'],
            'password': data['password']
        }
        self.client.post('/register', data=payload)
class WebsiteUser(HttpLocust):
    host = 'http://debugtalk.com'
    task_set = UserBehavior
    user_data_queue = queue.Queue()
    for index in range(100):
        data = {
            "username": "test%04d" % index,
            "password": "pwd%04d" % index,
            "email": "test%04d@debugtalk.test" % index,
            "phone": "186%08d" % index,
        }
        user_data_queue.put_nowait(data)
    min_wait = 1000
    max_wait = 3000