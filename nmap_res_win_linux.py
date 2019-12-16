#! /usr/bin/python2.7
# -*- coding:utf-8 -*-
# Script permettant de récupérer les ip et hostname des réseaux Linux et Windows
# Auteur : Frederic Seguin
# Date : 10 Decembre 2019
# Version : 1.0


import nmap
import os

# appel et défintion de la fonction nmap
def get_nmap(options, ip, option):
    command = "nmap " + options + " " + ip + " " + option
    process = os.popen(command)
    results = str(process.read())
    return results

# appel de la fontion nmap
print(get_nmap(' -A --version-light', '192.168.0.2-10', ' -oX ip_linux.xml'))
print(get_nmap(' -A --version-light', '192.168.1.2-10', ' -oX ip_windows.xml'))

# appel de la commande grep
os.system('grep -E -o "([0-9]{1,3}[.]){3}[0-9]{1,3}" ip_linux.xml | sort -u > final_linux.txt')
os.system('grep -E -o "([0-9]{1,3}[.]){3}[0-9]{1,3}" ip_windows.xml | sort -u > final_windows.txt')
print('Fin de commande')
