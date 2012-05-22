#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
from urllib import urlencode
from oauth2 import Client, Consumer, Token

consumer_key = "";
consumer_secret = "";
user_key = "";
user_secret = "";

client = Client(Consumer(consumer_key,consumer_secret), Token(user_key,user_secret))
argvs = sys.argv
for argv in argvs:
  print argv
message = "play " + argvs[2] + " from " + argvs[3] + "(" + argvs[1] + ")" + " ＠ " + argvs[4] + "回" + " #実験中 "

#message2 = "play " + argvs[2] + " from " + argvs[3] + " ＠ " + argvs[4] + "回" + " #実験中 "
client.request('http://api.twitter.com/1/statuses/update.xml', 'POST', urlencode({'status':message}))
#else:
#   client.request('http://api.twitter.com/1/statuses/update.xml', 'POST', urlencode({'status':message2}))
