#! /usr/bin/python2.7
# -*- coding:utf-8 -*-
# Script permettant la création de nouveaux utilisateurs Linux
# Auteur : Frederic Seguin
# Date : 10 Decembre 2019
# Version : 1.0


# import des modules
from pexpect import pxssh
import getpass
import os

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
    s.sendline('useradd -m ' + str(user)) # ajout de l'utilisateur
    s.sendline('passwd ' + str(user)) # création du pwd du nouvel utilisateur
    s.sendline('Frederic16..') # attribution du pwd
    s.sendline('Frederic16..') # confirmation du pwd
    s.sendline('passwd --unlock ' + str(user)) # activation de l'utilisateur
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("utilisateur créé.")


