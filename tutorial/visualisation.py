import xml.etree.ElementTree as ET



def evolution_cotes(fichier_xml,our_match):

    print("start")
    tree = ET.parse('resultats_paris_2/' + fichier_xml)
    root = tree.getroot()
    print(root.find("./match[@name='" + our_match + "']/cotes/victoire").text)
    print(root.find("./match[@name='" + our_match + "']/cotes/null").text)
    print(root.find("./match[@name='" + our_match + "']/cotes/defaite").text)

    tree = ET.parse('resultats_paris_2/winamax1646137463.xml')
    root = tree.getroot()
    print(root.find("./match[@name='" + our_match + "']/cotes/victoire").text)
    print(root.find("./match[@name='" + our_match + "']/cotes/null").text)
    print(root.find("./match[@name='" + our_match + "']/cotes/defaite").text)
    
evolution_cotes("winamax.xml","Sporting PortugalFC Porto")