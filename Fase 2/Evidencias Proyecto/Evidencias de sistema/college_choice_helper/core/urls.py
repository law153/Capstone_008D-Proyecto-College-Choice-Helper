from django.urls import path,include
from django.conf.urls import handler404
from .views import mostrarIndex

urlpatterns = [
    path('', mostrarIndex, name='index'),
]