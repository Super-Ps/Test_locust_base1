#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/11/10

import  sys

import pymysql

from locust import  HttpLocust ,TaskSet,task

# from locust_test.mysql_testdata_a import *



import  queue

class UserAction(TaskSet):

    def on_start(self):
        pass



    @task(2)
    def get_login(self):

        # 从队列里get出来列表数据
        get_data = self.locust.qu_object.get()

        #print("从队列拿到的数据：",get_data)
        # 获取列表里+1的下标
        #self.a_index=(self.index+1) % len(get_data)

        # # 拿到列表里的+1的下标对应的数据
        # row_parm=get_data[self.a_index]

        #print('row_parm：',row_parm)
        postdata = {
                    "username": get_data[1],
                    "password": get_data[2],
                    "passwordConfirm": get_data[3],
                    "firstName": get_data[4],
                    "lastName": get_data[5],
                    "address1": get_data[6],
                    "address2": get_data[7],
                    "register.x": get_data[8],
                    "register.y": get_data[9],
                      }

        print("注册用户账号是 username:{},password:{},firstName:{},lastName:{},address1:{},address2:{}"
              .format(get_data[1], get_data[2],
                      get_data[3], get_data[4],
                      get_data[5], get_data[6]))
        r_response = self.client.post('/login.pl', postdata)

        #html_text = r_response.text
        #print('html:',html_text)


class Userinstans(HttpLocust):

    def selectdata(rowno):
        # listdata=[]

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

    host ='http://127.0.0.1:1080/WebTours'
    task_set = UserAction

    # 实例化 Queue对象
    qu_object = queue.Queue(-1)

    # 获取数据库数据列表
    list_responsdata = selectdata(1000)
    for x in list_responsdata:
    # 非阻塞写入队列
        qu_object.put_nowait(x)
        #print( "放在队列的数据是：",x)
    min_wait = 1000
    max_wait = 5000