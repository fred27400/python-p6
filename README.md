# Projet 6 - AIC Openclassrooms
#
# Automatiser la gestion utilisateur et la sauvegarde de dossiers Windows/Linux    
# 
#
#
# Ce script Python à été créé afin d'effectuer des sauvegardes de manières automatisé et simple, il permet aussi la gestion des utilisateurs.                                                    
# Un fenetrage tkinter(projet6.py) permet d'avoir un menu des différents scripts d'automatisation.
#                                                                                                 
#                                                                                                 
# Ecrit par : Frederic Seguin
#                                  
# Date de création : 05/11/2019
#
# Dernière modification : 26/11/2019
#
# Testé avec : Python 2.7                                                                         
#                                                                                                 
# Ce propgramme/scripts sont sous Licence Publique Générale GNU V3
#
#
#
# Fonctionemment du script
Mettre les différents script sous un même dossier.
Lancez le script projet6.py en tout premier. Il vous affichera la fenetre de gestion des différents scripts d'automatisation.

#![ScreenShot](https://github.com/fred27400/python-p6/blob/master/photo/menu.png)

Ces différents scripts ont été écrit pour un réseau constitué d'une machine Linux ubuntu 18.04 desktop gérant deux réseaux en 192.168.0.0/24 (linux) et 192.168.1.0/24 (windows)

Un menu tkinter se lancant sur la machine linux ubuntu 18.04 desktop vous permet de lancer les différents scripts d'automatisation, il se trouve sur projet6.py. Il contient différents menus :
# .  Reseau
# .  Windows_users
# .  Linux_users
# .  Sauvegarde
# .  Quitter
# .  A propos
#      
Le menu Reseau, contient à ce jour un script Nmap pour deux sous réseau (un reseau linux, un reseau windows)
#
#![ScreenShot](https://github.com/fred27400/python-p6/blob/master/photo/reseau.png)
#
#Le menu windows-users, contient à ce jour 4 scripts : Liste utilisateur windows, Creation utilisateur AD, Activation utilisateur AD, Supression utilisateur AD.
#
![ScreenShot](https://github.com/fred27400/python-p6/blob/master/photo/windows_users.png)
#
#Le menu linux-users, contient à ce jour 3 scripts : Liste utilisateur linux, Création utilisateur linux, Suppression utilisateur linux.
#
#![ScreenShot](https://github.com/fred27400/python-p6/blob/master/photo/linux_users.png)
#
#Le menu Sauvegarde, contient à ce jour 2 scripts : Sauvegarde linux dossier home, Sauvegarde windows dossier données.
#
#![ScreenShot](https://github.com/fred27400/python-p6/blob/master/photo/sauvegarde.png)
#
#Tous ces scripts se lancent via une connexion ssh ou pexpect pxssh ou une connexion ldap distant.



     
     . 

