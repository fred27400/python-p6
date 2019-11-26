#! /usr/bin/python3.8
# -*- coding:utf-8 -*-
import Tkinter
import os


def show_about():
    about_window = Tkinter.Toplevel(app)
    about_window.title("A propos")
    lb = Tkinter.Label(about_window, text="Ce script automatise l'administration de windows ou de linux!!! \n\nCréateur : Mr Frédéric Seguin \n\nProjet 6 AIC Openclassrooms ")
    lb.pack()


def users_list():
    os.system('python2.7 listutilsad.py')


def create_utils():
    os.system('python2.7 createutilswin.py')


def activ_utils():
    os.system('python2.7 activutilswin.py')


def suppr_utils():
    os.system('python2.7 supprutilswin.py')


def sauv_win():
    os.system('python 2.7 sauvegardewin.py')


def list_users():
    os.system('python2.7 listutilslinux.py')


def create_users():
    os.system('python2.7 creatutilslinux.py')


def suppr_users():
    os.system('python2.7 supprutilslinux.py')


def sauv_linux():
    os.system('python2.7 sauvegardelinux.py')

def nmap_grep():
    os.system('python2.7 nmap_res_win_linux.py')


# Création de la fenêtre + paramétrage
app = Tkinter.Tk()
app.geometry("520x50")
app.title("Python Script Automatisation Windows/Linux")



# Widgets...
mainmenu = Tkinter.Menu(app)

# Premier menu
Reseau = Tkinter.Menu(mainmenu, tearoff=0)
Reseau.add_command(label="Decouverte reseau", command=nmap_grep)

# Deuxieme menu
Windows_users = Tkinter.Menu(mainmenu, tearoff=0)
Windows_users.add_command(label="Liste utilisateur AD", command=users_list)
Windows_users.add_command(label="Création utilisateur AD", command=create_utils)
Windows_users.add_command(label="Activation utilisateur AD", command=activ_utils)
Windows_users.add_command(label="Suppression utilisateur AD", command=suppr_utils)

# Troisième menu
Linux_users = Tkinter.Menu(mainmenu, tearoff=0)
Linux_users.add_command(label="Liste utilisateur Linux", command=list_users)
Linux_users.add_command(label="Création utilisateur Linux", command=create_users)
Linux_users.add_command(label="Suppression utilisateur Linux", command=suppr_users)

# quatrième menu
Sauvegarde = Tkinter.Menu(mainmenu, tearoff=0)
Sauvegarde.add_command(label="Sauvegarde Linux dossier home", command=sauv_linux)
Sauvegarde.add_command(label="Sauvegarde Win dossier users", command=sauv_win)

# Cinquième menu
Quitter = Tkinter.Menu(mainmenu, tearoff=0)
Quitter.add_command(label="Quitter", command=app.quit)

# Sixième menu
A_propos = Tkinter.Menu(mainmenu, tearoff=0)
A_propos.add_command(label="A propos", command=show_about)

mainmenu.add_cascade(label="Reseau", menu=Reseau)
mainmenu.add_cascade(label="Windows_users", menu=Windows_users)
mainmenu.add_cascade(label="Linux_users", menu=Linux_users)
mainmenu.add_cascade(label="Sauvegarde", menu=Sauvegarde)
mainmenu.add_cascade(label="Quitter", menu=Quitter)
mainmenu.add_cascade(label="A propos", menu=A_propos)

# Boucle principale
app.config(menu=mainmenu)
app.mainloop()
