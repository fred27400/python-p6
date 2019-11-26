#! /usr/bin/python2.7
# -*- coding:utf-8 -*-

from pexpect import pxssh
import getpass

user = raw_input('user: ')

try:
    s = pxssh.pxssh()
    hostname = raw_input('hostname: ')
    username = raw_input('username: ')
    password = getpass.getpass('password: ')
    s.login(hostname, username, password)
    s.sendline('su')   # lancez une commande
    s.sendline('Frederic16..')
    s.sendline('userdel -f -r ' + str(user))
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("utilisateur supprimé.")
    print(e)

