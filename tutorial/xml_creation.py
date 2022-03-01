import time
import xml
import xml.etree.cElementTree as ET

def creer_xml(site,list_noms, list_cotes, liste_joueurs, list_dates, list_championnats):
    #On creer le fichier xml
    
    root = ET.Element("root")
    for i in range(len(list_noms)):
        match = ET.SubElement(root, "div", name="match")
        ET.SubElement(match, "cotes", name = "cotes_site").text = list_noms[i]
        cotes = ET.SubElement(match, "cotes", name="cotes")
        ET.SubElement(cotes,"victoire").text = list_cotes[3 * i]
        ET.SubElement(cotes,"null").text = list_cotes[3 * i+1]
        ET.SubElement(cotes,"defaite").text = list_cotes[3 * i+2]
        cotes_joueurs = ET.SubElement(match, "cotes", name="cotes_joueurs")
        ET.SubElement(cotes_joueurs,"victoire").text = liste_joueurs[3 * i]
        ET.SubElement(cotes_joueurs,"null").text = liste_joueurs[3 * i+1]
        ET.SubElement(cotes_joueurs,"defaite").text = liste_joueurs[3 * i+2]
        ET.SubElement(match,"date").text = list_dates[i]
        ET.SubElement(match,"championnat").text = list_championnats[i]

    tree = ET.ElementTree(root)
    tree.write(site+str(time.asctime()) +".xml")