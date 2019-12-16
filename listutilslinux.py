#! /usr/bin/python2.7
# -*- coding:utf-8 -*-
# Script permettant la récupération des utilisateurs Linux
# Auteur : Frederic Seguin
# Date : 10 Decembre 2019
# Version : 1.0


# import des modules
from pexpect import pxssh
import getpass

# connexion en ssh au client linux
try:
    s = pxssh.pxssh()
    hostname = raw_input('hostname: ') # attribution variable hostname
    username = raw_input('username: ') # attribution variable username
    password = getpass.getpass('password: ') # attribution variable password
    s.login(hostname, username, password)
    s.sendline("cat /etc/passwd | awk -F: '{print $ 1}'") # impression des utilisateurs linux
    s.prompt()
    print(s.before)
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)
