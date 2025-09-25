from django.urls import path,include
from django.conf.urls import handler404
from .views import mostrarIndex, mostrarLogin, mostrarRegistro, mostrarOlvidoClave, inicioSesion, registrarUsuario
from .viewsEstu import mostrarFormularioEstudiante, mostrarRecomendaciones, mostrarVistaInstituciones, mostrarCambioClave, mostrarCambioCorreo, mostrarGestionCuenta, mostrarHacerPeticion
from .viewsInsti import mostrarRegistroInstitucion, mostrarEditarInstitucion, insertarInsti
from .viewsAdmin import mostrarGestionEstu, mostrarGestionInsti, mostrarVerPeticiones, mostrarVerPeticion

urlpatterns = [
    #SinCuenta
    path('', mostrarIndex, name='mostrarIndex'),
    path('inicio_sesion/', mostrarLogin, name='mostrarLogin'),
    path('registro/', mostrarRegistro, name='mostrarRegistro'),
    path('olvide_clave/', mostrarOlvidoClave, name="mostrarOlvide_clave"),
    path('inicioSesion/', inicioSesion, name='inicioSesion'),
    path('registrarUsuario/', registrarUsuario, name='registrarUsuario'),
    #Estudiante
    path('formulario_estudiante/', mostrarFormularioEstudiante, name='mostrarFormularioEstudiante'),
    path('recomendaciones/', mostrarRecomendaciones, name='mostrarRecomendaciones'),
    path('ver_institucion/', mostrarVistaInstituciones, name='mostrarVistaInstituciones'),
    path('cambio_clave/', mostrarCambioClave, name="mostrarCambioClave"),
    path('cambio_correo/', mostrarCambioCorreo, name="mostrarCambioCorreo"),
    path('gestion_cuenta/', mostrarGestionCuenta, name="mostrarGestionCuenta"),
    path('hacer_peticion/', mostrarHacerPeticion, name="mostrarHacerpeticion"),
    #Instituciones
    path('agregar_institucion/', mostrarRegistroInstitucion, name="mostrarRegistroInstitucion"),
    path('editar_institucion/', mostrarEditarInstitucion, name="mostrarEditarInstitucion"),
    path('insertar_institucion/', insertarInsti, name="insertarInsti"),
    #Admin
    path('gestionar_estu/', mostrarGestionEstu, name="mostrarGestionEstu"),
    path('gestionar_insti/', mostrarGestionInsti, name="mostrarGestionInsti"),
]