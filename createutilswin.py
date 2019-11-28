#! /usr/bin/python2.7
# -*- coding:utf-8 -*-

# Import des modules pour l'excecution du script
import ldap
import ldap.modlist as modlist

# Création de la variable adduser
adduser = raw_input('adduser: ')

# ouvre la connexion ldap du serveur windows 192.168.1.2
print('initializing ..')
conn = ldap.initialize('ldap://192.168.1.2')
conn.protocol_version = 3
conn.set_option(ldap.OPT_REFERRALS, 0)
conn.simple_bind_s('Administrateur@aicp5.local', 'Frederic16..')

# Dn du nouvel utilisateur
DN = ('CN=' + str(adduser) + ',OU=utilisateurs,DC=aicp5,DC=local')

# attribue du nouvel utilisateur
modlist = {
    'objectClass': ['top', 'person', 'organizationalPerson', 'user'],
    'cn': str(adduser),
    'givenName': str(adduser),
    'displayName': str(adduser),
    'sAMAccountName': str(adduser),
    'userAccountControl': '514',
    'userPrincipalName': (str(adduser) + '@aicp5.local'),
    'mail': (str(adduser) + '@aicp5.local'),
    'userPassword': 'Frederic16..',
    'description': 'test',
    'pwdLastSet': '-1'
}

# Creation du nouvel utilisateur
result = conn.add_s(DN, ldap.modlist.addModlist(modlist))
print('Utilisateur créé')
exit
