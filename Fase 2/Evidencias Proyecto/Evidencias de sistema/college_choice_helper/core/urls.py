from django.urls import path,include
from django.conf.urls import handler404
from .views import mostrarIndex, mostrarLogin, mostrarRegistro, mostrarOlvidoClave
from .viewsEstu import mostrarFormularioEstudiante, mostrarRecomendaciones, mostrarVistaInstituciones, mostrarCambioClave, mostrarCambioCorreo, mostrarGestionCuenta
from .viewsInsti import mostrarRegistroInstitucion, mostrarEditarInstitucion

urlpatterns = [
    path('', mostrarIndex, name='index'),
    path('inicio_sesion/', mostrarLogin, name='login'),
    path('registro/', mostrarRegistro, name='registro'),
    path('formulario_estudiante/', mostrarFormularioEstudiante, name='formulario_estudiante'),
    path('recomendaciones/', mostrarRecomendaciones, name='recomendaciones'),
    path('ver_institucion/', mostrarVistaInstituciones, name='ver_instituciones'),
    path('agregar_institucion/', mostrarRegistroInstitucion, name="agregar_institucion"),
    path('editar_institucion/', mostrarEditarInstitucion, name="editar_institucion"),
    path('cambio_clave/', mostrarCambioClave, name="cambio_clave"),
    path('cambio_correo/', mostrarCambioCorreo, name="cambio_correo"),
    path('gestion_cuenta/', mostrarGestionCuenta, name="gestion_cuenta"),
    path('olvide_clave/', mostrarOlvidoClave, name="olvide_clave"),
]