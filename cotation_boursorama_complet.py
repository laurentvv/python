# -*-coding:utf-8 -*
# Laurent VOLFF
# 09/06/2016

import urllib
from bs4 import BeautifulSoup
import sys
import datetime
import sqlite3
from mme import mme
from macd import macd

# On récupère les données de http://www.boursorama.com/cours.phtml?symbole=1rPTEC
sock = urllib.urlopen("http://www.boursorama.com/cours.phtml?symbole=1rPTEC")
htmlSource = sock.read()                            
sock.close()
soup = BeautifulSoup(htmlSource, 'html.parser')

# On cherche table puis span, filtre pour retrouver la zone où se trouve les infos de cotation sur la page
table = soup.find("table")
span = table.findAll("span")

# span[?] emplacement de l'info cherchée sur la page contents[0] recup le contenu split et replace pour enlevé € et espace 
action = soup.find(itemprop="name").get_text()
cotation = float(span[1].contents[0].split()[0])
volume = int(span[4].contents[0].replace(" ", ""))
ouverture = float(span[6].contents[0].split()[0])
haut = float(span[8].contents[0].split()[0])
bas = float(span[10].contents[0].split()[0])
cloture_veille = float(span[12].contents[0].split()[0])
date = datetime.datetime.now()

# Récupération dans la base les valeurs de la dernière cotation
d = "{2}-{1}-{0}".format(date.day,date.month,date.year)
conn = sqlite3.connect(r'e:\doc\technip.db')
c = conn.cursor()
t = (d,)
c.execute('select mme20,mme12,mme26 from cotation where date < ? order by date DESC LIMIT 1', t)
mme_veille_20, mme_veille_mme12, mme_veille_mme26 = c.fetchone()
conn.close()

mme20 = mme(20,mme_veille_20,cotation)
mme12 = mme(12,mme_veille_mme12,cotation)
mme26 = mme(26,mme_veille_mme26,cotation)
macd = macd(mme12,mme26)

# On affiche
print("{}\n".format(action))
print("Cotation : {}\n".format(cotation))
print("Date : {0}/{1}/{2} \n".format(date.day,date.month,date.year))
print("Volume : {}\n".format(volume))
print("Ouverture : {}\n".format(ouverture))
print("Haut : {}\n".format(haut))
print("Bas : {}\n".format(bas))
print("Cloture de la veille : {}\n".format(cloture_veille))
print("Variation : {}".format((( cotation - cloture_veille ) / cotation ) * 100))

# INSERTION dans base SQLITE
conn = sqlite3.connect(r'e:\doc\technip.db')
c = conn.cursor()

# Pour la création de la BDD
#c.execute('''CREATE TABLE cotation
#             (nom text, cotation real, date text, volume int, ouverture real, haut real, bas real, clotureveille real, mme real)''')
             
# Insert a row of data
c.execute("REPLACE INTO cotation VALUES ('{}',{},'{}-{}-{}',{},{},{},{},{},{},{},{},{})".format(action,cotation,date.year,date.month,date.day,volume,ouverture,haut,bas,cloture_veille,mme20,mme12,mme26,macd))
conn.commit()
conn.close()
