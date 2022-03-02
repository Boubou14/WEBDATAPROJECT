from gettext import find
import os
import time
import xml.etree.ElementTree as ET

list = os.listdir('resultats_paris_2/')
print(time.ctime(1646161979))

list_winamax = []
list_unibet = []

for e in list:
    if e[0]=="u":
        list_unibet.append(e)
    else:
        list_winamax.append(e)

dict = {}

for e in list_unibet:
    tree = ET.parse("resultats_paris_2/"+e)
    root = tree.getroot()
    list_match = (root.findall("match"))
    for match in list_match:
        if float(match.find("cotes/victoire").text.replace(",",".")) > 10:
            root.remove(match)
        if float(match.find("cotes/null").text.replace(",",".")) > 10:
            root.remove(match)
        if float(match.find("cotes/defaite").text.replace(",",".")) > 10:
            root.remove(match)

    tree.write('resultats_paris_2/'+ e)