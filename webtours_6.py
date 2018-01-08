#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/10/19

from locust import HttpLocust, TaskSet, task
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

        html_text = self.client.get('/nav.pl?in=home').text
        re_session = self.get_login_session(html_text)
        print('获取session值：%s' % re_session)

        data = {
            "userSession": re_session,
            "username": "jonny10011",
            "password": "jy123456",
            "login.x": "52",
            "login.y": "7",
            "login": "Login",
            "JSFormSubmit": "off",
        }
        with self.client.post("/login.pl", data, catch_response=True) as r_response:
            print('获取login返回值：%s' % r_response.text)
            re_html_text = r_response.text
            etree_text = etree.HTML(re_html_text)
            r_text = etree_text.xpath("//frame[@src][2]")
            print(r_text)
            # 取列表元素,调用 ResponseContextManager类方法判断
            for x in r_text:
                r_x = x.values()[0]
                print('获取元素b：', r_x, end='')
                if r_x == 'login.pl?intro=true':
                    r_response.success()
                else:
                    r_response.failure(" failure")


class WebUser(HttpLocust):
    host = "http://127.0.0.1:1080/WebTours/"
    task_set = WebUserAction
    min_wait = 1000
    max_wait = 3000


    '''
    <html>
<title>Web Tours</title>
<frameset cols="160,*" border=1 frameborder=1>
<frame src=nav.pl?page=menu&in=home name=navbar marginheight=2 marginwidth=2 noresize scrolling=auto>
<frame src=login.pl?intro=true name=info marginheight=2 marginwidth=2 noresize scrolling=auto>
</frameset>

</body>
</html>
    '''

    '''
    <html>
<title>Web Tours</title>
<frameset cols="160,*" border=1 frameborder=1>
<frame src=nav.pl?username=jonny111&password=jy123456 name=navbar marginheight=2 marginwidth=2 noresize scrolling=auto>
<frame src=error.pl?error=badPassword name=info marginheight=2 marginwidth=2 noresize scrolling=auto>
</frameset>

</body>
</html>
    
    '''