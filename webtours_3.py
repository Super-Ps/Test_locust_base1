#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/10/16

from locust import HttpLocust, TaskSet, task,events
import queue
from lxml import etree

# 注册业务 保证并发测试数据唯一性，不循环取数据
class WebActionUser(TaskSet):

    @task
    def user_pl(self):
        try:
            # 获取队列，
            get_data = self.locust.user_data_q.get()
            print('从队列里面拿到的数据',get_data)
            print('他是类型是：', type(get_data))
        except queue.Empty:
            print("参数错误,直接退出")
            exit(0)
        # 通过get拿到队列数据，构造成postdata
        queue_data = {
                    "username": get_data["username"],
                    "password": get_data["password"],
                    "passwordConfirm": get_data["passwordConfirm"],
                    "firstName": get_data["firstName"],
                    "lastName": get_data["lastName"],
                    "address1": get_data["address1"],
                    "address2": get_data["address2"],
                    "register.x": get_data["register.x"],
                    "register.y": get_data["register.y"],
                      }
        # 格式化展示调试
        print("注册用户账号是 username:{},password:{},firstName:{},lastName:{},address1:{},address2:{}"
              .format(get_data['username'], get_data["password"],
            get_data["firstName"], get_data["lastName"],
            get_data["address1"], get_data["address2"]))
        with self.client.post('/login.pl', queue_data,catch_response=True) as r_response:
            html_text = r_response.text
            # html解析
            r_html = etree.HTML(html_text)
            # print('返回html对象：', r_html)
            # xpath方法定位截取
            r_text = r_html.xpath("//blockquote")
            # 取列表元素,调用 ResponseContextManager类方法判断
            for x in r_text:
                r_x = x.text
                # print('获取元素：', r_x, end='')
                if r_x == 'Thank you,':
                    r_response.success()
                else:
                    r_response.failure("failure")
        # 将数据再次put到队列
        #self.locust.user_data_q.put_nowait(queue_data)


class WebUser(HttpLocust):

    host = "http://127.0.0.1:1080/WebTours"
    task_set = WebActionUser
    # 获取队列对象
    user_data_q = queue.Queue()
    # 生成请求递增参数,格式化设定整型d
    for index_x in range(20, 30):
        pl_data = {"username": "jonnyc70%d" % index_x,
                   "password": "jy123456",
                   "passwordConfirm": "jy123456",
                   "firstName": "jyc0%d" % index_x,
                   "lastName": "psc0%d" % index_x,
                   "address1": "zgszA0%d" % index_x,
                   "address2": "CityStateZipnA0%d" %index_x,
                   "register.x": "35",
                   "register.y": "18",
                   }
        # 等价于 Queue.put(item, False)   非阻塞写入队列，
        user_data_q.put_nowait(pl_data)

        print('放在队列里的数据：',pl_data)
        print('他是类型是：',type(pl_data))
    min_wait = 1000
    max_wait = 3000


