#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/11/9

import pymysql

# 查询数据库所有数据

def selectdata(rowno):

    #listdata=[]

    conn = pymysql.connect(host='192.168.64.131', port=3306, user='root', passwd='123456', db='makeblock',
                           charset='utf8')
    # 创建游标
    cursor = conn.cursor()
    cursor.execute("select * from  webtoursd ")
    # 结果的第一行
    #re_row = cursor.fetchone()
    # 结果的前几行，参数指定
    re_row = cursor.fetchmany(rowno)

    # 全部结果
    #re_row = cursor.fetchall()
    #print('获取数据库返回数据：', list(re_row))

    conn.commit()

    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

    return re_row


# a=selectdata(5)
#
# print(a)
# print()
# print("第一次：",next(a))
# print("第2次：",next(a))
# print("第3次：",next(a))
# print("第4次：",next(a))