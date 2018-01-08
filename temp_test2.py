#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/10/11



from  lxml import etree

import re

import requests

def lxml_html():


    html = "http://127.0.0.1:1080/WebTours/"

    r = requests.get(html)
    print(r)
    re_text=r.text

    re_html = etree.HTML(re_text)
    href_a = re_html.xpath(u"//frame")
    print(type(href_a))
    for x in href_a:

        recv_href = x.text
        print(type(recv_href))
        recv_hrefa = x.attrib
        print(recv_hrefa)
        # if not "":
        #     x_x=recv_href
        #     return x_x

x=lxml_html()
print(x)
print(type(x))



#help(re)



