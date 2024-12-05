import pytest

from solver import generate_valid_words


def test_generate_valid_words_start_d():
    """On sait que la première lettre du mot est un D"""
    assert generate_valid_words(
        possible_words=["DEVANT", "ENTREE", "PORTER", "GAUCHE"],
        letters_in_secret=[('D', 0)],
        letters_not_in_secret=[]
    ) == ["DEVANT"]

def test_generate_valid_words_possible_words_empty():
    """Test de la liste vide pour possible_words"""
    assert generate_valid_words(
        possible_words=[],
        letters_in_secret=[],
        letters_not_in_secret=[]
    ) == []

def test_generate_valid_words_no_letters_played():
    """Test pour vérifier que la liste de mots possibles reste inchangée lorsqu'aucune lettre n'est jouée"""
    assert generate_valid_words(
        possible_words=["PLAINDRE", "PAUPIERE", "QUARANTE"],
        letters_in_secret=[],
        letters_not_in_secret=[]
    ) == ["PLAINDRE", "PAUPIERE", "QUARANTE"]

def test_generate_valid_words_with_letters():
    """Test du filtrage des mots suivant les lettres inclues et exclues"""
    assert generate_valid_words(
        possible_words=["FIGURER", "HAUTEUR", "CROISER", "MEMOIRE", "PLONGER"],
        letters_in_secret=[('R',6),('O',2)],
        letters_not_in_secret=["F", "H","M"]
    ) == ["CROISER", "PLONGER"]