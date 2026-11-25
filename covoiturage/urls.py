from django.urls import path  # noqa: F401

from . import views  # noqa: F401

app_name = "covoiturage"

urlpatterns = [
    path("", views.liste, name="liste"),
    path("trajet/<int:pk>/", views.detail, name="detail"),
]
