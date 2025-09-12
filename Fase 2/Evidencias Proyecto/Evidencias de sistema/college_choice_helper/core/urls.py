from django.urls import path,include
from django.conf.urls import handler404
from .views import mostrarIndex, mostrarLogin, mostrarRegistro

urlpatterns = [
    path('', mostrarIndex, name='index'),
    path('inicio_sesion/', mostrarLogin, name='login'),
    path('registro/', mostrarRegistro, name='registro'),
]