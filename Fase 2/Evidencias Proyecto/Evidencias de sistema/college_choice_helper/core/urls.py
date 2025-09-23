from django.urls import path,include
from django.conf.urls import handler404
from .views import mostrarIndex, mostrarLogin, mostrarRegistro, mostrarOlvidoClave, inicioSesion, registrarUsuario
from .viewsEstu import mostrarFormularioEstudiante, mostrarRecomendaciones, mostrarVistaInstituciones, mostrarCambioClave, mostrarCambioCorreo, mostrarGestionCuenta
from .viewsInsti import mostrarRegistroInstitucion, mostrarEditarInstitucion, insertarInsti
from .viewsAdmin import mostrarGestionEstu, mostrarGestionInsti

urlpatterns = [
    #SinCuenta
    path('', mostrarIndex, name='mostrarIndex'),
    path('inicio_sesion/', mostrarLogin, name='mostrarLogin'),
    path('registro/', mostrarRegistro, name='mostrarRegistro'),
    path('olvide_clave/', mostrarOlvidoClave, name="mostrarOlvide_clave"),
    path('inicioSesion/', inicioSesion, name='inicioSesion'),
    path('registrarUsuario/', registrarUsuario, name='registrarUsuario'),
    #Estudiante
    path('formulario_estudiante/', mostrarFormularioEstudiante, name='formulario_estudiante'),
    path('recomendaciones/', mostrarRecomendaciones, name='recomendaciones'),
    path('ver_institucion/', mostrarVistaInstituciones, name='ver_instituciones'),
    path('cambio_clave/', mostrarCambioClave, name="cambio_clave"),
    path('cambio_correo/', mostrarCambioCorreo, name="cambio_correo"),
    path('gestion_cuenta/', mostrarGestionCuenta, name="gestion_cuenta"),
    #Instituciones
    path('agregar_institucion/', mostrarRegistroInstitucion, name="agregar_institucion"),
    path('editar_institucion/', mostrarEditarInstitucion, name="editar_institucion"),
    path('insertar_institucion/', insertarInsti, name="insertar_institucion"),
    #Admin
    path('gestionar_estu/', mostrarGestionEstu, name="gestionar_estu"),
    path('gestionar_insti/', mostrarGestionInsti, name="gestionar_insti"),
]