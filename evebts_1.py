#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/10/19

from locust import HttpLocust, TaskSet, events, task
import random, traceback

def on_request_success(request_type, response_time, response_length):
    print ('Type: %s, Name: %s, Time: %fms, Response Length: %d' %
            request_type,  response_time, response_length)
# #
# def on_request_failure(request_type, name, response_time, exception):
#     print('Type: %s, Name: %s, Time: %fms, Reason: %r' % (request_type, name, response_time, exception))
# #
# def on_locust_error(locust_instance, exception, tb):
#     print ("%r, %s, %s" % (locust_instance, exception, "".join(traceback.format_tb(tb))))
# #
# def on_hatch_complete(user_count):
#     print ("Haha, Locust have generate %d users" % user_count)
# #
# def on_quitting():
#     print ("Locust is quiting")

events.request_success += on_request_success
# events.request_failure += on_request_failure
# events.locust_error += on_locust_error
# events.hatch_complete += on_hatch_complete
# events.quitting += on_quitting


class UserTask(TaskSet):
    @task(5)
    def job1(self):
        with self.client.get('/', catch_response = True) as r:
            if random.choice([0, 1]):
                r.success()
            else:
                r.failure('0')

    @task(1)
    def job2(self):
        raise Exception("Mars Loo's test")

class User(HttpLocust):
    task_set = UserTask
    min_wait = 3000
    max_wait = 5000
    host = 'http://127.0.0.1:1080/WebTours'