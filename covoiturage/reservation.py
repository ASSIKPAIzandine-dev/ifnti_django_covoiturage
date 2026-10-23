from django.db import models
from .models import Trajet


class Reservation(models.Model):
    nom = models.CharField(max_length=200)
    nombre_place_reserver = models.BigIntegerField()
    
    trajet = models.ForeignKey(
        Trajet, on_delete=models.CASCADE, related_name="reservations"
    )
    
