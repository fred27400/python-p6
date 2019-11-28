#! /usr/bin/python2.7
# -*- coding:utf-8 -*-

# Import des modules pour l'execution du script
import ldap
import ldap.modlist as modlist
import sys

# création de la variable user
user = raw_input('user: ')

# ouvre la connexion ldap du serveur windows 192.168.1.2
print('initializing ..')
conn = ldap.initialize('ldap://192.168.1.2')
conn.protocol_version = 3
conn.set_option(ldap.OPT_REFERRALS, 0)
conn.simple_bind_s('Administrateur@aicp5.local', 'Frederic16..')

# Dn de l'utilisateur à activer
DN = ('CN=' + str(user) + ',OU=utilisateurs,DC=aicp5,DC=local')

# activation de l'utilisateur
ATTR = 'userAccountControl'
ATT_VALUE = '4096'
userAccountControl = [(ldap.MOD_REPLACE, ATTR, [ATT_VALUE])]
result = conn.modify(DN, userAccountControl)
print('Compte utilisateur activé')
