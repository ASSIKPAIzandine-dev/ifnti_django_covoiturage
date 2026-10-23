from covoiturage.models import Trajet,Reservation
import pytest
from django.core.exceptions import ValidationError


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


def test_trajet_propose_au_moins_une_place(db):

    trajet = Trajet.objects.create(
        conducteur="assikpa",
        ville_depart="sokodé",
        ville_arrivee="kara",
        date_depart="2026-10-23",
        heure_depart="8:00",
        places=3,
        prix_place=5000,
    )
    if trajet.places is not None and trajet.places < 1:
        raise ValidationError("Un trajet propose au moins une place.")


def test_affichage_trajet(db):

    trajet = Trajet.objects.create(
        conducteur="assikpa",
        ville_depart="sokodé",
        ville_arrivee="Lomé",
        date_depart="2026-11-23",
        heure_depart="20:00",
        places=5,
        prix_place=5000,
    )
    assert trajet


def test_creation_d_une_reservation(db):

    trajet = Trajet.objects.create(
        conducteur="KODjo",
        ville_depart="sokodé",
        ville_arrivee="kara",
        date_depart="2026-11-23",
        heure_depart="09:00",
        places=2,
        prix_place=2500,
    )

    # reservation = Reservation.objects.create(
    #     nom="kossi", nombre_place_reserver=2, trajet=trajet
    # )
    
    reservation = Reservation.objects.create(
    trajet=trajet,
    nom="Kossi",
    nombre_place_reserver=2
    )
    assert str(reservation) == "Kossi : 2 places"
    
    
def test_passager_ne_peut_pas_reserver_deux_fois_le_meme_trajet(db):
    
        trajet = Trajet.objects.create(
                conducteur="abass",
                ville_depart="sokodé",
                ville_arrivee="kara",
                date_depart="2026-11-23",
                heure_depart="10:00",
                places=3,
                prix_place=2500,
            )
        
        Reservation.objects.create(
            trajet=trajet,
            nom="Kossi",
            nombre_place_reserver=1
        )
        double_reservation = Reservation(
        trajet=trajet,
        nom="Kossi",
        nombre_place_reserver=2
        )
 