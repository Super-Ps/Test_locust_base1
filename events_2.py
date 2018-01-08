#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/10/20
from locust import Locust, TaskSet, events, task

mars_event = events.EventHook()

def mars_special_event(verb = '', content = ''):
    print ('mars %s %s' % (verb, content))

mars_event += mars_special_event

class UserTask(TaskSet):
    @task(1)
    def job1(self):
        mars_event.fire(verb = 'love', content = 'locust')

    @task(3)
    def job2(self):
        print ("In job2 ...")

class User(Locust):
    task_set = UserTask
    min_wait = 3000
    max_wait = 5000