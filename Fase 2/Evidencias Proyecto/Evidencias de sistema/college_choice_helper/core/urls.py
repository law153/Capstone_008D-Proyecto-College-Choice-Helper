from django.urls import path,include
from django.conf.urls import handler404
from .views import mostrarIndex, mostrarLogin, mostrarRegistro, mostrarOlvidoClave, inicioSesion, registrarUsuario
from .viewsEstu import mostrarFormularioEstudiante, mostrarRecomendaciones, mostrarVistaInstituciones, mostrarCambioClave, mostrarCambioCorreo, mostrarGestionCuenta, mostrarHacerPeticion, cierreSesion, generarPeticion
from .viewsInsti import mostrarRegistroInstitucion, mostrarEditarInstitucion, insertarInsti, actualizarInsti
from .viewsAdmin import mostrarGestionEstu, mostrarGestionInsti, mostrarVerPeticiones, mostrarVerPeticion, cambiarRol

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
    path('cierre_sesion/', cierreSesion, name="cierreSesion"),
    path('generar_peticion/', generarPeticion, name="generarPeticion"),
    #Instituciones
    path('agregar_institucion/', mostrarRegistroInstitucion, name="mostrarRegistroInstitucion"),
    path('editar_institucion/<id_insti>', mostrarEditarInstitucion, name="mostrarEditarInstitucion"),
    path('insertar_institucion/', insertarInsti, name="insertarInsti"),
    path('actualizar_institucion/', actualizarInsti, name="actualizarInsti"),
    #Admin
    path('gestionar_estu/', mostrarGestionEstu, name="mostrarGestionEstu"),
    path('gestionar_insti/', mostrarGestionInsti, name="mostrarGestionInsti"),
    path('ver_peticiones/', mostrarVerPeticiones, name="mostrarVerPeticiones"),
    path('ver_peticion/<idPeticiones>', mostrarVerPeticion, name="mostrarVerPeticion"),
    path('cambiar_rol/<idPeticion>/<correo>', cambiarRol, name="cambiarRol"),
]