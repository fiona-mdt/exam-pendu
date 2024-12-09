import math
from copy import copy

def generate_valid_words(possible_words: list[str], letters_in_secret: list[tuple[str, int]], letters_not_in_secret: list[str]) -> list[str]:
    """
    Génère une liste de mots valides à partir de la liste de mots potentiels, 
    en fonction des lettres déjà trouvées et des lettres exclues.
    """
    if not possible_words:  # Vérification si la liste possible_words est vide
        return []
    
    mots_valides = []
    
    lettres_exclues = set(letters_not_in_secret)  # Création d'un ensemble pour letters_not_in_secret pour vérifier rapidement les lettres

    for mot in possible_words:
        est_valide = True
        
        for lettre in lettres_exclues:  # Vérification du mot pour voir s'il ne contient pas de lettres exclues
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



def generate_best_letters(possible_words: list, letters_not_played: list[str], letters_in_secret: list[tuple[str, int]], letters_not_in_secret: list[str]) -> str:
    """
    Suggère la meilleure lettre à jouer basée sur les fréquences moyennes des lettres dans la liste des mots valides.
    """
    letter_freq = {letter: 0 for letter in letters_not_played}  # Initialisation d'un dictionnaire pour compter les occurrences des lettres non jouées
    
    for mot in possible_words:  # Parcourt des mots valides pour compter les occurrences des lettres non jouées
        for lettre in letters_not_played:
            letter_freq[lettre] += mot.count(lettre)
    
    # Calcul de la fréquence moyenne de chaque lettre
    average_freq = { 
        letter: letter_freq[letter] / len(possible_words)
        for letter in letter_freq
    } 
    
    # Recherche de la lettre qui a la fréquence moyenne la plus élevée
    best_letter = None
    max_freq = 0  # Initialisation de max_freq à 0 pour comparer les fréquences
    for letter in average_freq:  # Comparaison des lettres
        if average_freq[letter] > max_freq:
            max_freq = average_freq[letter]
            best_letter = letter
    
    return f"Essayez de jouer : {best_letter}"

# Commentaire Bonus