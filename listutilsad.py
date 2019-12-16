#! /usr/bin/python2.7
# -*- coding:utf-8 -*-
# Script permettant le lancement du script liste utilisateurs windows
# Auteur : Frederic Seguin
# Date : 10 Decembre 2019
# Version : 1.0


import os

os.system("ssh Administrateur@192.168.1.2 'py -s' <./listutilsad1.py")   # lancez une commande
