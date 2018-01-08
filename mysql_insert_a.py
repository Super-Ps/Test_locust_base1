#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/11/9

import pymysql

#  批量生产对应字段数据，插入数据库中，便于取数据

def insetmysql(a, b):

    for x in range(a, b):
        str_x = str(x)
        usernamea = 'peng2000'+str_x
        passworda= 'p123456'
        passwordConfirma='p123456'
        firstNamea ='peng'
        lastNamea ='s10'+str_x
        address1a='深圳市南山智源C3-10000'+str_x
        address2a='广东省10000'+str_x
        registerxa='52'
        registerya='8'
        conn = pymysql.connect(host='192.168.64.131', port=3306,
                               user='root', passwd='123456',
                               db='makeblock', charset='utf8')
        # 创建游标
        cursor = conn.cursor()
        # 插入数据
        re_row = cursor.execute("INSERT into  webtoursd(username, password,passwordConfirm, "
                                "firstName, lastName, address1, address2, registerx, registery"
                                ")VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s )"
                                    , (usernamea, passworda, passwordConfirma,
                                       firstNamea, lastNamea, address1a, address2a,
                                       registerxa, registerya))
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()

#获取自增id
# new_id = cursor.lastrowid
# print (new_id)
insetmysql(1, 50000000)