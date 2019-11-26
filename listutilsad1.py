#! /usr/bin/python2.7
# -*- coding:utf-8 -*-

import os

os.system('net user > users.txt')
users = Path('./users.txt').read_text()
print(users)


