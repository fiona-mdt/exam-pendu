import pytest

from generate_dicts import lire_filtrer_mots


def test_lire_filtrer_mots_file_empty():
    """Test du message d'erreur lorsque la fonction lit un fichier vide"""
    try:
        lire_filtrer_mots(
            chemin_lexique="data_test/filetest_empty.txt",
            longueur=6
        )
    except ValueError as erreur:
        assert str(erreur) == "Erreur : le fichier data_test/filetest_empty.txt est vide."

def test_lire_filtrer_mots_correct_length():
    """Test des mots de longueur 7"""
    assert lire_filtrer_mots(
        chemin_lexique="data_test/filetest2.txt",
        longueur=7
    ) == {"ACCUSER", "TOUCHER", "ARTICLE"}

def test_lire_filtrer_mots_no_special_characters():
    """Test des mots sans caractère spéciaux"""
    assert lire_filtrer_mots(
        chemin_lexique="data_test/filetest4.txt",
        longueur=9
    ) == {"EVENEMENT", "LENDEMAIN", "APPARENCE"}

def test_lire_filtrer_mots_spaces():
    """Test du traitement des espaces avant ou après les mots"""
    assert lire_filtrer_mots(
        chemin_lexique="data_test/filetest1.txt",
        longueur=6
    ) == {"ECOUTE", "ARRETE", "CAMION"}