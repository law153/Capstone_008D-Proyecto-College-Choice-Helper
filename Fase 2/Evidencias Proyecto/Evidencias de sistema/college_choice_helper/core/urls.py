from django.urls import path,include
from django.conf.urls import handler404
from .views import mostrarIndex, mostrarLogin, mostrarRegistro, mostrarRecomendaciones, mostrarVistaInstituciones, mostrarFormularioEstudiante

urlpatterns = [
    path('', mostrarIndex, name='index'),
    path('inicio_sesion/', mostrarLogin, name='login'),
    path('registro/', mostrarRegistro, name='registro'),
    path('formulario_estudiante/', mostrarFormularioEstudiante, name='formulario_estudiante'),
    path('recomendaciones/', mostrarRecomendaciones, name='recomendaciones'),
    path('ver_institucion/', mostrarVistaInstituciones, name='ver_instituciones'),
]