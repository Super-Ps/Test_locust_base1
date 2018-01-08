#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/10/13

import requests





def func_t():
    headers = {'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3408.400 QQBrowser/9.6.12028.400',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded'}

    url ="http://127.0.0.1:1080/WebTours/login.pl"
    data = {'username': 'jonny10011',
            'password': 'jy123456',
            'passwordConfirm': 'jy123456',
            'firstName': 'jonny3',
            'lastName': 'ps3',
            'address1': 'Street + Address + no10003',
            'address2': 'CityStateZipno10003',
            'register.x': '52',
            'register.y': '8'
            }
    re=requests.post(url,data=data,headers=headers)
    print(re.text)


a=func_t()
print(a)