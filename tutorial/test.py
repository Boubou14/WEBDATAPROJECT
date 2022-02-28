import time
import xml
import xml.etree.cElementTree as ET

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class match_class:
    def _init_(self):
        nom = ""
        championnat = ""
        date = ""
        cote_victoire = ""
        cote_null = ""
        cote_defaite = ""
        cote_victoire_votant =""
        cote_null_votant =""
        cote_defaite_votant =""


driver = webdriver.Firefox()
driver.get("https://www.unibet.fr/sport/football")

SCROLL_PAUSE_TIME = 2

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


list_noms = driver.find_elements_by_xpath("//div[@class='cell-event']/span")
list_cotes = driver.find_elements_by_xpath("//span[@class='ui-touchlink-needsclick price odd-price']")
list_dates = driver.find_elements_by_class_name("datetime")
list_championnats = driver.find_elements_by_xpath("//span[@class='competition']")
liste_joueurs = driver.find_elements_by_tag_name("strong")

"""
for i in range(10):
    print(list_noms[i].text)
    print(list_cotes[3 * i].text + "  " + list_cotes[3 * i +1].text + "  " + list_cotes[3 * i+2].text)
    print(liste_joueurs[3+3*i].text + "  " + liste_joueurs[3+3*i +1].text + "  " + liste_joueurs[3+3*i+2].text)
    print(list_dates[i].text)
    print(list_championnats[i].text)"""

for i in range(10):
    match = match_class
    match.nom = (list_noms[i].text)
    match.cote_victoire = list_cotes[3 * i].text
    match.cote_null = list_cotes[3 * i +1].text
    match.cote_defaite = list_cotes[3 * i+2].text
    match.cote_victoire_votant = liste_joueurs[3 * i].text
    match.cote_null_votant = liste_joueurs[3 * i +1].text
    match.cote_defaite_votant = liste_joueurs[3 * i+2].text
    match.date = list_dates[i].text
    match.championnat = list_championnats[i].text

#On creer le fichier xml
root = ET.Element("root")
for i in range(len(list_noms)):
    match = ET.SubElement(root, "div", name="match")
    ET.SubElement(match, "cotes", name = "cotes_site").text = list_noms[i].text
    cotes = ET.SubElement(match, "cotes", name="cotes")
    ET.SubElement(cotes,"victoire").text = list_cotes[3 * i].text
    ET.SubElement(cotes,"null").text = list_cotes[3 * i+1].text
    ET.SubElement(cotes,"defaite").text = list_cotes[3 * i+2].text
    cotes_joueurs = ET.SubElement(match, "cotes", name="cotes_joueurs")
    ET.SubElement(cotes_joueurs,"victoire").text = liste_joueurs[3 * i].text
    ET.SubElement(cotes_joueurs,"null").text = liste_joueurs[3 * i+1].text
    ET.SubElement(cotes_joueurs,"defaite").text = liste_joueurs[3 * i+2].text
    ET.SubElement(match,"date").text = list_dates[i].text
    ET.SubElement(match,"championnat").text = list_championnats[i].text

tree = ET.ElementTree(root)
tree.write("filename.xml")

driver.close()