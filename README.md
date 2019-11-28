# python-p6

################################################################################################### 
#                                                                                                 #
# #######  automatiser la gestion utilisateur et la sauvegarde de dossier windows/linux    ########
#                                                                                                 #
# #################################################################################################
#                                                                                                 #
# Ce script Python à été créé afin d'effectuer des sauvegardes de manières automatisé et simple,  #
# il permet aussi la gestion des utilisateurs.                                                    #
# Un fenetrage tkinter(projet6.py) permet d'avoir un menu des différents scripts d'automatisation.#
#                                                                                                 #
# #################################################################################################
#                                                                                                 #
# Ecrit par : Frederic Seguin                                                                     #                                  
# Date de création : 05/11/2019                                                                   #
# Dernière modification : 26/11/2019                                                              #
# Testé avec : Python 2.7                                                                         #
#                                                                                                 #
# #################################################################################################

Ces différents scripts ont été écrit pour un réseau constitué d'une machine Linux ubuntu 18.04 
desktop gérant deux réseaux en 192.168.0.0/24 (linux) et 192.168.1.0/24 (windows)

Un menu tkinter se lancant sur la machine linux ubuntu 18.04 desktop vous permet de lancer les 
différents scripts d'automatisation, il se trouve sur projet6.py.
Il contient différents menus :
     .  Reseau
     .  Windows_users
     .  Linux_users
     .  Sauvegarde
     .  Quitter
     .  A propos
     
Le menu Reseau, contient à ce jour un script Nmap pour deux sous réseau (un reseau linux, un reseau windows)
Le menu windows-users, contient à ce jour 4 scripts :
     . Liste utilisateur windows
     . Creation utilisateur AD 
     . Activation utilisateur AD
     . Supression utilisateur AD
Le menu linux-users, contient à ce jour 3 scripts :
     . Liste utilisateur linux
     . Création utilisateur linux
     . Suppression utilisateur linux
Le menu Sauvegarde, contient à ce jour 2 scripts :
     . Sauvegarde linux dossier home
     . Sauvegarde windows dossier données
     
Tous ces scripts se lancent via une connexion ssh ou pexpect pxssh ou une connexion ldap distant.



     
     . 

