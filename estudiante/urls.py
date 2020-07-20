from django.conf.urls import url
from estudiante import views

urlpatterns = [
    url('', views.vista_estudiante)
]
