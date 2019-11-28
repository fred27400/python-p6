#! /usr/bin/python2.7
# -*- coding:utf-8 -*-

# import des modules
from pexpect import pxssh
import getpass

# création de la variable user
user = raw_input('user: ')

# connexion en ssh au client linux
try:
    s = pxssh.pxssh()
    hostname = raw_input('hostname: ') # attribution variable hostname
    username = raw_input('username: ') # attribution variable username
    password = getpass.getpass('password: ') # attribution variable password
    s.login(hostname, username, password)
    s.sendline('su')   # passage en admin
    s.sendline('Frederic16..') # mdp admin
    s.sendline('userdel -f -r ' + str(user)) # suppression de l'utilisateur et de ses dossiers
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("utilisateur supprimé.")
    print(e)

