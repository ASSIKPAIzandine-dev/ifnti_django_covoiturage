from datetime import date, time

import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction

from covoiturage.models import Reservation, Trajet


def donnees(**kw):
    d = dict(
        conducteur="izandine",
        ville_depart="Sokodé",
        ville_arrivee="Lomé",
        date_depart=date(2026, 11, 23),
        heure_depart=time(12, 10),
        places=4,
        prix_place=3000,
    )
    d.update(kw)
    return d


def un_trajet(**kw):
    return Trajet.objects.create(**donnees(**kw))


def test_creation_d_un_trajet(db):
    t = un_trajet()
    t.refresh_from_db()
    assert t.pk is not None
    assert (t.conducteur, t.ville_depart, t.ville_arrivee) == (
        "izandine",
        "Sokodé",
        "Lomé",
    )
    assert t.date_depart == date(2026, 11, 23)
    assert t.heure_depart == time(12, 10)
    assert (t.places, t.prix_place) == (4, 3000)


@pytest.mark.parametrize("places", [0, -1])
def test_trajet_sans_place_est_refuse(db, places):

    with pytest.raises(ValidationError):
        Trajet(**donnees(places=places)).full_clean()


def test_trajet_avec_une_seule_place_est_accepte(db):
    Trajet(**donnees(places=1)).full_clean()


def test_affichage_trajet(db):
    assert (
        str(un_trajet(date_depart=date(2026, 11, 23), heure_depart=time(12, 10)))
        == "Sokodé:Lomé: le 2026-11-23: à 12:10"
    )


def test_creation_d_une_reservation(db):
    t = un_trajet(places=2)
    r = Reservation.objects.create(trajet=t, nom="Kossi", nombre_place_reserver=2)
    r.refresh_from_db()
    assert (r.trajet, r.nom, r.nombre_place_reserver) == (t, "Kossi", 2)


def test_passager_ne_peut_pas_reserver_deux_fois_le_meme_trajet(db):
    t = un_trajet()
    Reservation.objects.create(trajet=t, nom="Kossi", nombre_place_reserver=1)
    with pytest.raises(IntegrityError), transaction.atomic():
        Reservation.objects.create(trajet=t, nom="Kossi", nombre_place_reserver=2)
    assert Reservation.objects.count() == 1


def test_un_conducteur_peut_proposer_plusieurs_trajets(db):

    Trajet.objects.create(
        conducteur="Ama",
        ville_depart="Sokodé",
        ville_arrivee="Lomé",
        date_depart=date(2026, 12, 1),
        heure_depart=time(7, 0),
        places=4,
        prix_place=3000,
    )
    Trajet.objects.create(
        conducteur="Ama",
        ville_depart="Sokodé",
        ville_arrivee="Kara",
        date_depart=date(2026, 12, 5),
        heure_depart=time(8, 0),
        places=3,
        prix_place=2000,
    )
    assert Trajet.objects.filter(conducteur="Ama").count() == 2


def test_deux_passagers_differents_sur_le_meme_trajet(db):
    t = un_trajet()
    Reservation.objects.create(trajet=t, nom="Kossi", nombre_place_reserver=1)
    Reservation.objects.create(trajet=t, nom="Afi", nombre_place_reserver=1)
    assert t.reservations.count() == 2

