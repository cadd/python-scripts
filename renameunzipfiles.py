# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:12:17 2015

@author: robert
"""

import os
import datetime
import zipfile

#Files umbenennen und nach Alt-Ordner verschieben
for filename in os.listdir("."):
    if filename.startswith("UMSATZ"):
        t = os.path.getmtime(filename)
        v = datetime.datetime.fromtimestamp(t)
        x = v.strftime('%Y%m%d-%H%M%S')
        os.rename(filename, "X://01_Immo//Coba-Daten//Pythontest//old//" +
                  x + "-" + filename)

#Download-Zip entpacken
zfile = zipfile.ZipFile("C://Users//robert//Downloads//UMSATZ.zip")
zfile.extractall("C://Users//robert//Downloads")
zfile.close()

#Entpackte Datei in Coba-Daten-Verzeichnis verschieben
os.rename("C://Users//robert//Downloads//UMSATZ.txt",
          "X://01_Immo//Coba-Daten//Pythontest//UMSATZ.txt")
