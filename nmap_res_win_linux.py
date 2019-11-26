#! /usr/bin/python2.7
# -*- coding:utf-8 -*-

import nmap
import os


def get_nmap(options, ip, option):
    command = "nmap " + options + " " + ip + " " + option
    process = os.popen(command)
    results = str(process.read())
    return results


print(get_nmap(' -A --version-light', '192.168.0.2-10', ' -oX ip_linux.xml'))
print(get_nmap(' -A --version-light', '192.168.1.2-10', ' -oX ip_windows.xml'))

os.system('grep -E -o "([0-9]{1,3}[.]){3}[0-9]{1,3}" ip_linux.xml | sort -u > final_linux.txt')
os.system('grep -E -o "([0-9]{1,3}[.]){3}[0-9]{1,3}" ip_windows.xml | sort -u > final_windows.txt')
print('Fin de commande')
