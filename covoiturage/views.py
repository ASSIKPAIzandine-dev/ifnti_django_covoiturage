from django.shortcuts import get_object_or_404, redirect, render  # noqa: F401
from django.db.models import Q
from django.utils import timezone
from .models import Trajet


def liste(request):
    now = timezone.localtime()
    trajets = Trajet.objects.filter(
        Q(date_depart__gt=now.date())
        | Q(date_depart=now.date(), heure_depart__gt=now.time())
    ).order_by("date_depart", "heure_depart")
    return render(request, "covoiturage/liste.html", {"trajets": trajets})


def detail(request, pk):
    trajet = get_object_or_404(Trajet, pk=pk)
    return render(request, "covoiturage/detail.html", {"trajet": trajet})
