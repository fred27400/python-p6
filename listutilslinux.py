#! /usr/bin/python2.7
# -*- coding:utf-8 -*-

from pexpect import pxssh
import getpass

try:
    s = pxssh.pxssh()
    hostname = raw_input('hostname: ')
    username = raw_input('username: ')
    password = getpass.getpass('password: ')
    s.login(hostname, username, password)
    s.sendline("cat /etc/passwd | awk -F: '{print $ 1}'")
    s.prompt()
    print(s.before)
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)
