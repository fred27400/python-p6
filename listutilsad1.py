#! /usr/bin/python2.7
# -*- coding:utf-8 -*-
# Script permettant la récupération de la liste utilisateurs Windows
# Auteur : Frederic Seguin
# Date : 10 Decembre 2019
# Version : 1.0


# import des modules
import os

# envoi de la commande pour sortir la liste des utilisateurs
os.system('net user')
print('liste des utilisateurs')


