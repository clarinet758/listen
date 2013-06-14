#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
from urllib import urlencode
from oauth2 import Client, Consumer, Token

consumer_key = ""
consumer_secret = ""
user_key = ""
user_secret = ""

client = Client(Consumer(consumer_key, consumer_secret), Token(user_key, user_secret))
argvs = sys.argv

message = "play " + argvs[2] + " from " + argvs[3] + "(" + argvs[1] + ")" + " ＠" + argvs[4] + "回" + " #任意のタグ "
client.request('https://api.twitter.com/1.1/statuses/update.json', 'POST', urlencode({'status': message}))
