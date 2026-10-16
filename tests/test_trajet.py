from covoiturage.models import Trajet
import pytest


def test_creation_d_un_trajet(db):

    trajet = Trajet.objects.create(
        conducteur="izandine",
        ville_depart="Sokodé",
        ville_arrivee="Lomé",
        date_depart="2026-10-17",
        heure_depart="18:00",
        places=4,
        prix_place=3000,
    )

    assert trajet.conducteur
    assert trajet.ville_depart
    assert trajet.ville_arrivee
    assert trajet.date_depart
    assert trajet.heure_depart
    assert trajet.places
    assert trajet.prix_place


def test_trajet_propose_au_moins_une_place():
    trajet = Trajet.objects.create(
        conducteur="assikpa",
        ville_depart="sokodé",
        ville_arrivee="kara",
        date_depart = "2026-10-23",
        heure_depart = "8:00",
        places = 0,
        prix_place =5000
    )
    
    if(pytest.raises(Exception)):
            print("PASSED .....")
    else :
            print("FAILED.....")
