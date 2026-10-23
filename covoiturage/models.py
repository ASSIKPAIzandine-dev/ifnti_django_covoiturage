from django.db import models  
class Trajet(models.Model):

    conducteur = models.CharField(unique=True)
    ville_depart = models.CharField(max_length=80)
    ville_arrivee = models.CharField(max_length=80)
    
    date_depart = models.DateField()
    heure_depart = models.CharField()
    places = models.BigIntegerField(max_length=80)
    prix_place = models.BigIntegerField(max_length=80)
    
    def __str__(self):
        return f"{self.ville_depart}-({self.ville_arrivee}) , le {self.date_depart} à {self.heure_depart}"
    


class Reservation(models.Model):
    nom = models.CharField(max_length=200)
    nombre_place_reserver = models.BigIntegerField()
    
    trajet = models.ForeignKey(
        Trajet, on_delete=models.CASCADE, related_name="reservations"
    )
    
    class Meta:
        constraints = [
        models.UniqueConstraint(
        fields=["trajet", "nom"],
        name="unique_passager_par_trajet"
        )
    ]

    def __str__(self):
        return f"{self.nom} : {self.nombre_place_reserver} places"
