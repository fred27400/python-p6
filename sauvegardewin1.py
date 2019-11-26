#! /usr/bin/python2.7
# -*- coding:utf-8 -*-

import sys
import os
import shutil
import time
import tarfile

class BackUp(object):
    def __init__(self):
        self.source = "d:\\donnees"
        self.target = "c:\\backups"
        if os.path.isdir(self.source):
            fld_name = self.get_target_name()
            print('fld_name')
            self.save_archiv(fld_name)

    def get_target_name(self):
        tl = time.localtime()
        return "save_%s-%s_%s-%s-%s.tar.gz" % (tl.tm_hour, tl.tm_min,
                                                                 tl.tm_year, tl.tm_mon, tl.tm_mday)

    def save_archiv(self, fld):
        target = os.path.join(self.target, fld)
        if os.path.isdir(target):
            print("Un dossier du même nom existe déjà")
            return
        os.chdir(os.path.dirname(self.source))
        tar = tarfile.open(target, "w:gz")
        tar.add(os.path.basename(self.source))
        tar.close()


if __name__ == "__main__":
    bckp = BackUp()
    print("Done")
