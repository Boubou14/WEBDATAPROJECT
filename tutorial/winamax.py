import time
import outils

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from xml_creation import creer_xml

options = webdriver.FirefoxOptions()
options.add_argument("headless")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Firefox(options=options)
driver.get("https://www.winamax.fr/paris-sportifs/sports/1")

time.sleep(5)
"""
driver.find_element_by_xpath("//button[@class='sc-kTLXwr giFOuQ']").click()
time.sleep(2)
driver.find_element_by_xpath("//p[@class='sc-euehnN dxXwnp']").click()
time.sleep(2)"""
SCROLL_PAUSE_TIME = 1

last_height = driver.execute_script("return document.body.scrollHeight")
indent = 0
while True:
    indent +=1
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, "+str(5000*indent)+")")
    if indent >2:
        break
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return window.pageYOffset + window.innerHeight")
    if new_height == last_height:
        time.sleep(5)
        if new_height == last_height:
            break
    last_height = new_height


list_noms1 = outils.get_text_list(driver.find_elements_by_xpath("//span[@class='sc-kMOkjD sc-czgevV jZjyro ivSlSu']"))
list_noms2 = outils.get_text_list(driver.find_elements_by_xpath("//span[@class='sc-kMOkjD sc-jHMygC jZjyro hhnEbP']"))
list_noms = [list_noms1[i]+list_noms2[i] for i in range(len(list_noms1))]
list_cotes = outils.get_text_list(driver.find_elements_by_xpath("//span[@class='sc-iAjKSQ hTLTCG']"))
list_dates = outils.get_text_list(driver.find_elements_by_xpath("//div[@class='sc-dqxvKW jdsnAX timer']"))
list_championnats = outils.get_text_list(driver.find_elements_by_xpath("//div[@class='sc-eZuTdo fQQjvN sc-zzdIa derPWs']"))
liste_joueurs = outils.get_text_list(driver.find_elements_by_xpath("//span[@class='sc-dmqUwf gVqMhg']"))


outils.afficher_resultat_10(list_noms, list_cotes, liste_joueurs, list_dates, list_championnats)
creer_xml("winamax",list_noms, list_cotes, liste_joueurs, list_dates, list_championnats)

driver.close()
