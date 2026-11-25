from django.core.validators import MinValueValidator
from django.db import models


class Trajet(models.Model):
    conducteur = models.CharField(max_length=100)
    ville_depart = models.CharField(max_length=100)
    ville_arrivee = models.CharField(max_length=100)
    date_depart = models.DateField()
    heure_depart = models.TimeField()
    places = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    prix_place = models.PositiveIntegerField(help_text="En francs CFA")

    def __str__(self):
        return (
            f"{self.ville_depart}:{self.ville_arrivee}: "
            f"le {self.date_depart}: à {self.heure_depart:%H:%M}"
        )


class Reservation(models.Model):
    trajet = models.ForeignKey(
        Trajet, on_delete=models.CASCADE, related_name="reservations"
    )
    nom = models.CharField(max_length=100)
    nombre_place_reserver = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["trajet", "nom"], name="un_passager_par_trajet"
            ),
        ]
def __str__(self):
    mot = "place" if self.nombre_place_reserver == 1 else "places"
    return f"{self.nom} : {self.nombre_place_reserver} {mot}"