import xml.etree.ElementTree as ET



tree = ET.parse('unibetMon Feb 28 22.09.42 2022.xml')
root = tree.getroot()


fils1 =root.findall("./div")
list_noms = []
list_cotes = []
liste_joueurs = []
list_championnats = []
list_dates = []
for fils in fils1:
    list_noms.append(fils.find("cotes").text)
    list_cotes.append(fils.find("cotes/victoire").text)
    list_cotes.append(fils.find("cotes/null").text)
    list_cotes.append(fils.find("cotes/defaite").text)
    if fils.find("cotes[@name='cotes_joueurs']/victoire").text == None:
        liste_joueurs.append(None)
    elif fils.find("cotes[@name='cotes_joueurs']/victoire").text[0] != "R":
        liste_joueurs.append(fils.find("cotes[@name='cotes_joueurs']/victoire").text)
    liste_joueurs.append(fils.find("cotes[@name='cotes_joueurs']/null").text)
    liste_joueurs.append(fils.find("cotes[@name='cotes_joueurs']/defaite").text)
    list_dates.append(fils.find("date").text)
    list_championnats.append(fils.find("championnat").text)


root = ET.Element("root")
for i in range(len(list_noms)):
    try:
        match = ET.SubElement(root, "match", name=list_noms[i])
        cotes = ET.SubElement(match, "cotes")
        ET.SubElement(cotes,"victoire").text = list_cotes[3 * i]
        ET.SubElement(cotes,"null").text = list_cotes[3 * i+1]
        ET.SubElement(cotes,"defaite").text = list_cotes[3 * i+2]
        cotes_joueurs = ET.SubElement(match, "cotes_joueurs")
        ET.SubElement(cotes_joueurs,"victoire").text = liste_joueurs[3 * i]
        ET.SubElement(cotes_joueurs,"null").text = liste_joueurs[3 * i+1]
        ET.SubElement(cotes_joueurs,"defaite").text = liste_joueurs[3 * i+2]
        ET.SubElement(match,"date").text = list_dates[i]
        ET.SubElement(match,"championnat").text = list_championnats[i]    
    except:
        break
tree = ET.ElementTree(root)
tree.write("yeess" +".xml")

