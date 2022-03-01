
def afficher_resultat_10(list_noms, list_cotes, liste_joueurs, list_dates, list_championnats):
    for i in range(10):
        print(list_noms[i])
        print(list_cotes[3 * i]  + "  " + list_cotes[3 * i +1]  + "  " + list_cotes[3 * i+2] )
        print(liste_joueurs[3+3*i]  + "  " + liste_joueurs[3+3*i +1]  + "  " + liste_joueurs[3+3*i+2] )
        print(list_dates[i] )
        print(list_championnats[i] )

def get_text_list(selen):
    return [e.text for e in selen]