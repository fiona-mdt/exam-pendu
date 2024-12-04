import math
from copy import copy

def generate_valid_words(possible_words: list[str], letters_in_secret: list[tuple[str, int]], letters_not_in_secret: list[str]) -> list[str]:
    """
    Génère une liste de mots valides à partir de la liste de mots potentiels, 
    en fonction des lettres déjà trouvées et des lettres exclues.
    """
    mots_valides = []
    
    lettres_exclues = set(letters_not_in_secret) # Création d'un ensemble pour letters_not_in_secret pour vérifier rapidement les lettres

    for mot in possible_words:
        est_valide = True
        
        for lettre in lettres_exclues: # Vérification du mot pour voir s'il ne contient pas de lettres exclues
            if lettre in mot:
                est_valide = False
                break
        
        if est_valide: # Vérification de la position des lettres
            for lettre, position in letters_in_secret:
                if mot[position] != lettre:
                    est_valide = False
                    break
        
        if est_valide:
            mots_valides.append(mot)
    
    return mots_valides



def generate_best_letters(possible_words:list, letters_not_played:list[str], letters_in_secret, letters_not_in_secret):
    return "Ajoutez votre implémentation ici"









