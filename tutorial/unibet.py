import time
import outils

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from xml_creation import creer_xml





driver = webdriver.Firefox()
driver.get("https://www.unibet.fr/sport/football")

time.sleep(5)

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


list_noms = outils.get_text_list(driver.find_elements_by_xpath("//div[@class='cell-event']/span"))
list_cotes = outils.get_text_list(driver.find_elements_by_xpath("//span[@class='ui-touchlink-needsclick price odd-price']"))
list_dates = outils.get_text_list(driver.find_elements_by_class_name("datetime"))
list_championnats = outils.get_text_list(driver.find_elements_by_xpath("//span[@class='competition']"))
liste_joueurs = outils.get_text_list(driver.find_elements_by_tag_name("strong"))


outils.afficher_resultat_10(list_noms, list_cotes, liste_joueurs, list_dates, list_championnats)
creer_xml("unibet",list_noms, list_cotes, liste_joueurs, list_dates, list_championnats)

driver.close()
