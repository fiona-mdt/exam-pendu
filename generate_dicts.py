from unidecode import unidecode

"""
Depuis le fichier liste_mots.txt, on récupère tous les mots de 6,7,8,9,10 lettres.
et on génère 5 fichiers textes contenant les mots en fonction de leur taille (un mot par ligne, séparé par un \n):
dico_6_lettres.txt
dico_7_lettres.txt
dico_8_lettres.txt
dico_9_lettres.txt
dico_10_lettres.txt
On enlève les accents, les espaces, les tirets et les mots en double.
"""

def lire_filtrer_mots(chemin_lexique: str, longueur: int) -> list[str]:
    """
    Lit les mots d'un fichier texte, les nettoie et filtre ceux qui ont une longueur spécifiée,
    en excluant les mots contenant des caractères spéciaux comme ' , - ou des espaces.
    """
    lst_test = []  # Liste pour stocker les mots valides
    
    with open(chemin_lexique, "r", encoding="utf-8") as f:
        for ligne in f:
            mots = ligne.split()  # Séparation de la ligne en mots
            if mots:  # Vérification de la présence de mots dans la ligne
                mot = mots[0]  # Prend le premier mot (les données après ne nous intéresse pas)

                if "'" in mot or "-" in mot or " " in mot: # Exclusion des mots contenant les caractères définis comme indésirables
                    continue

                mot = unidecode(mot).upper() # Nettoyage des accents et mise en majuscules des mots

                if len(mot) == longueur: # Filtrage par longueur et ajout à la liste si validé
                    lst_test.append(mot)   

    return set(lst_test) # Retour de la liste avec élimination des doublons



def ecrire_liste_mots(liste_mots:list, longueur:int) -> None:
    """Génère un fichier texte contenant tous les mots pour une longueur donné"""

    chemin_dico_ecriture:str = f"data/dico_{longueur}_lettres.txt"

    with open(chemin_dico_ecriture, 'w', encoding='utf-8') as file:
        file.writelines(f"{mot}\n" for mot in liste_mots)



def main(chemin:str) -> None:
    for long in range(6,11):
        # génère la liste de mot pour la longueur donné
        lst_mots = lire_filtrer_mots(chemin_lexique=chemin, longueur=long)

        # Génère un fichier texte correspondant
        ecrire_liste_mots(lst_mots, longueur=long)

if __name__ == '__main__':
    chemin = "data/liste_mots.txt"
    main(chemin= chemin)