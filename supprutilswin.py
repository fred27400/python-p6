#! /usr/bin/python2.7
# -*- coding:utf-8 -*-
# Script permettant la suppression utilisateur Windows Active Directory
# Auteur : Frederic Seguin
# Date : 10 Decembre 2019
# Version : 1.0

# Import des modules pour l'excecution du script
import ldap
import ldap.modlist as modlist

# création de la variable user
user = raw_input('user: ')

# ouvre la connexion ldap du serveur windows 192.168.1.2
print('initializing ..')
conn = ldap.initialize('ldap://192.168.1.2')
conn.protocol_version = 3
conn.set_option(ldap.OPT_REFERRALS, 0)
conn.simple_bind_s('Administrateur@aicp5.local', 'Frederic16..')

# Dn de l'utilisateur à supprimer
DN = ('CN=' + str(user) + ',OU=utilisateurs,DC=aicp5,DC=local')

# Suppression de l'utilisateur
conn.delete_s(DN)
print('utilisateur supprimé')
