#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/11/13

import pymysql
import queue
from locust import HttpLocust,TaskSet,task

from lxml import etree

# 演示登陆前截取服务器返回的sessionID,通过lxml解析得到参数,传递在登陆请求后再lxml遍历解析返回列表,判断作为检查点
class WebUserAction(TaskSet):

    def on_start(self):
        pass

    @staticmethod
    def get_login_session(html_text):
        text = etree.HTML(html_text)
        return text.xpath("//input[@name='userSession']/@value ")

    @task
    def user_login(self):
        # 从列表拿数据 ，类型是元组
        get_data = self.locust.qu_object.get()
        print('从队列拿到的数据',get_data)
        html_text = self.client.get('/nav.pl?in=home').text
        re_session = self.get_login_session(html_text)
        #print('获取session值：%s' % re_session)

        data = {
            "userSession": re_session,
            "username": get_data[1],
            "password": get_data[2],
            "login.x": "52",
            "login.y": "7",
            "login": "Login",
            "JSFormSubmit": "off",
        }
        print("获取的username是：%s,获取的usersession是：%s,获取的密码是：%s" % (re_session,get_data[1],get_data[2]))

        with self.client.post("/login.pl", data, catch_response=True) as r_response:
            print('获取login返回值：%s' % r_response.text)
            re_html_text = r_response.text
            etree_text = etree.HTML(re_html_text)
            r_text = etree_text.xpath("//frame[@src][2]")
            print(r_text)
            # 取列表元素,调用 ResponseContextManager类方法判断
            for x in r_text:
                r_x = x.values()[0]
                #print('获取元素b：', r_x, end='')
                if r_x == 'login.pl?intro=true':
                    r_response.success()
                else:
                    r_response.failure(" failure")
        # 循环put数据到队列
        self.locust.qu_object.put_nowait(get_data)
        print("再次put到队列的数据是：%s" % (get_data))

class WebUser(HttpLocust):

    def selectdata(rowno):

        conn = pymysql.connect(host='192.168.64.131', port=3306, user='root', passwd='123456', db='makeblock',
                               charset='utf8')
        # 创建游标
        cursor = conn.cursor()
        cursor.execute("select * from  webtoursd ")
        # 结果的第一行
        # re_row = cursor.fetchone()
        # 结果的前几行，参数指定
        re_row = cursor.fetchmany(rowno)
        # 全部结果
        # re_row = cursor.fetchall()
        # print('获取数据库返回数据：', list(re_row))
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        return re_row

    host = "http://127.0.0.1:1080/WebTours/"
    task_set = WebUserAction
    # 实例化 Queue对象
    qu_object = queue.Queue(-1)

    # 获取数据库数据列表
    list_responsdata = selectdata(50)
    for x in list_responsdata:
    # 非阻塞写入队列
        qu_object.put_nowait(x)
        print( "放在队列的数据是：",x)
    # min_wait = 1000
    # max_wait = 3000

# class WebUserA(HttpLocust):
#
#     min_wait =
#     max_wait =