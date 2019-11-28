#! /usr/bin/python2.7
# -*- coding:utf-8 -*-

# import des modules
import sys
import os
import shutil
import time
import tarfile

# utilisation de class pour extraire les données du système
class BackUp(object):   # définition de la classe backup pour la sauvegarde

    # définitions des attributs et méthodes

    def __init__(self): # définition des chemins
        self.source = "/home"
        self.target = "/mnt/backup"
        if os.path.isdir(self.source):
            fld_name = self.get_target_name()
            print fld_name
            self.save_archiv(fld_name)

    def get_target_name(self): # définition de l'heure et de la date
        tl = time.localtime()
        return "save_%s-%s_%s-%s-%s.tar.gz" % (tl.tm_hour, tl.tm_min,
                                                                 tl.tm_year, tl.tm_mon, tl.tm_mday)

    def save_archiv(self, fld): # définition de la mise en fichier tar.gz et vérification de l'existence du fichier à créer
        target = os.path.join(self.target, fld)
        if os.path.isdir(target):
            print "Un dossier du même nom existe déjà"
            return
        os.chdir(os.path.dirname(self.source))
        tar = tarfile.open(target, "w:gz")
        tar.add(os.path.basename(self.source))
        tar.close()


if __name__ == "__main__":
    bckp = BackUp()
    print "sauvegarde effectuée"

