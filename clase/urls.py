from django.urls import path
from clase import views

urlpatterns = [
    path("", views.vista_clase),
]