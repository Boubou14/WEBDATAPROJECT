from gettext import find
import os
import time
import xml.etree.ElementTree as ET

list = os.listdir('resultats_paris_2/')

list_winamax = []
list_unibet = []

for e in list:
    if e[0]=="u":
        list_unibet.append(e)
    else:
        list_winamax.append(e)

dict = {}



for e in list_winamax:
    tree = ET.parse("resultats_paris_2/"+e)
    root = tree.getroot()
    list_match = (root.findall("match"))
    for match in list_match:
        nom = match.attrib["name"]
        try:
            dict[nom].append(match.find("cotes/victoire").text)
        except:
            dict[nom] = []
            dict[nom].append(match.find("cotes/victoire").text)



change_max = 0
key_max = ""
for keys,list_match in dict.items():
    somme = 0
    cote_ini = float(list_match[0].replace(",","."))
    for i in range(1,len(list_match)):
        somme+= abs(cote_ini - float(list_match[i].replace(",",".")))
        cote_ini = float(list_match[i].replace(",","."))
    if somme > change_max:
        change_max = somme
        key_max = keys

print(change_max)
print(key_max)
print(dict[key_max])
