from covoiturage.models import Trajet


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


# def test_trajet_propose_au_une_place():
    