#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jonny"
# Email: jonnysps@yeah.net
# Date: 2017/10/10


import json

def function_json():

    json_a = {
        "logo": "/upload/org/126733b5-c5fa-4a58-8039-e32453ae634a.png",
        "teamNo": 0.5991032400160861,
        "name": "locust_1",
        "teamType": "primary",
        "slogan": "say:NB!",
        "introduce": "locust_1\\nsay:NB!\\nnumber_one\\n",
        "members": [
            {
                "photo": "/upload/org/c7b5136b-ecc6-4cad-8470-5a6b6a163bcd.png",
                "name": "tameb",
                "mobile": "(+86)13528427307",
                "phoneType": "(+86)",
                "idType": "idCard",
                "idNum": "43072319880604004X",
                "type": "member"
            },
            {
                "photo": "/upload/org/b5774195-6444-41b0-89e6-407f8dd84b44.png",
                "name": "tamec",
                "mobile": "(+86)13528427307",
                "phoneType": "(+86)",
                "idType": "idCard",
                "idNum": "43072319880604003X",
                "type": "member"
            },
            {
                "photo": "/upload/org/6b515feb-522f-4f37-9cc0-0b14b92ad97b.png",
                "name": "tamed",
                "mobile": "(+86)13528427307",
                "phoneType": "(+86)",
                "idType": "idCard",
                "idNum": "43072319880604002X",
                "type": "member"
            }
        ],
        "teachers": [
            {
                "photo": "/upload/org/5222a9f2-1edc-4576-b6b7-c6042162847a.png",
                "name": "locustaa",
                "mobile": "(+86)13528427307",
                "phoneType": "(+86)",
                "idType": "idCard",
                "idNum": "43072319880604006X",
                "type": "teacher"
            }
        ],
        "captain": {
            "photo": "/upload/org/f9a644e5-db3e-4a2c-acf9-7db1c6e15125.png",
            "name": "tamea",
            "mobile": "(+86)13528427307",
            "phoneType": "(+86)",
            "idType": "idCard",
            "idNum": "43072319880604005X",
            "type": "captain"
        }
    }
    return json_a



# print(type(json_a))
# #print(json.loads(json_a))
# json_a=json.dumps(json_a) #转化为json
# print(json_a)
# print(type(json_a))
#
# print("------------------------------")
# json_b=json.loads(json_a) #转化为字典
# print(json_b)
# print(type(json_b))

