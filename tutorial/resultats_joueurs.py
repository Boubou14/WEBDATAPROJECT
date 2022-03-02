from gettext import find
import os
import xml.etree.ElementTree as ET
import time
import outils

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.footmercato.net/live/2022-02-28")

time.sleep(5)
dict_score = {}


liste_score1 = driver.find_elements_by_xpath("//span[@class='matchItem__score__value matchItem__score__value--home']")
liste_score2 = driver.find_elements_by_xpath("//span[@class='matchItem__score__value matchItem__score__value--away']")

list_result1 = driver.find_elements_by_xpath("//span[@class='matchItem__team__name']")
list_result = [list_result1[i].text + " - " + list_result1[i+1].text for i in range(len(liste_score1))]

for i in range(len(liste_score1)):
    if int(liste_score1[i].text)> int(liste_score2[i].text): 
        dict_score[list_result[i]] = "victoire"
    elif int(liste_score1[i].text) ==  int(liste_score2[i].text): 
        dict_score[list_result[i]] = "null"
    else: 
        dict_score[list_result[i]] = "defaite"

list_winamax = []
list_unibet = []
list = os.listdir('resultats_paris_2/')

for e in list:
    if e[0]=="u":
        list_unibet.append(e)
    else:
        list_winamax.append(e)

dict = {}
somme =0
tree = ET.parse("resultats_paris_2/"+list_unibet[1])
root = tree.getroot()
list_match = (root.findall("match"))
nombre_match = 0
for match in list_match:
    nom = match.attrib["name"]
    if nom in dict_score:
        nombre_match +=1
        somme -= float(match.find("cotes/"+ dict_score[nom]).text)
        somme += 0.1 * float(match.find("cotes_joueurs/"+ dict_score[nom]).text.replace("%",""))

print(nombre_match)
print(somme)
driver.close()




