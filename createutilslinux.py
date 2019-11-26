#! /usr/bin/python2.7
# -*- coding:utf-8 -*-


from pexpect import pxssh
import getpass
import os

user = raw_input('user: ')

try:
    s = pxssh.pxssh()
    hostname = raw_input('hostname: ')
    username = raw_input('username: ')
    password = getpass.getpass('password: ')
    s.login(hostname, username, password)
    s.sendline('su')   # lancez une commande
    s.sendline('Frederic16..')
    s.sendline('useradd -m ' + str(user))
    s.sendline('passwd ' + str(user))
    s.sendline('Frederic16..')
    s.sendline('Frederic16..')
    s.sendline('passwd --unlock ' + str(user))
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("utilisateur créé.")


