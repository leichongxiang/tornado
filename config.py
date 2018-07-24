#coding:utf-8

import os

#application配置参数
settings = {
    "static_path":os.path.join(os.path.dirname(__file__), "static"),
    "template_path":os.path.join(os.path.dirname(__file__),"template"),
    "cookie_secret":"ScDhzx04SNm3e5InXphoV/HiKongLUM+jeyRSkem+3Y=",
    "xsrf_cookies":"GEv7wZtzTESci+STmqqyAnWBNU+hKUKPp/zOYmjlmu8=",
    "debug":True,
}

#mysql
mysql_options=dict(
    host="192.168.1.140",
    database="ihome",
    user="root",
    password="mysql"
)

#redis
redis_options = dict(
    host="192.168.1.140",
    port=6379
)