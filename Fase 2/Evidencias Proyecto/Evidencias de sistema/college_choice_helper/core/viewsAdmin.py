from django.shortcuts import render
from .models import Usuario, Rol, Peticiones, Institucion

#Admin
def mostrarGestionEstu(request):
    rol = request.session.get('rol', None)
    correo = request.session.get('correo', None)

    contexto = {'rol': rol, 'correo': correo}
    return render (request,'core/admin/gestionEstudiantes.html', contexto)

def mostrarGestionInsti(request):
    rol = request.session.get('rol', None)
    correo = request.session.get('correo', None)
    contexto = {'rol': rol, 'correo': correo}
    return render (request,'core/admin/gestionInstituciones.html', contexto)

def mostrarVerPeticiones(request):
    rol = request.session.get('rol', None)
    correo = request.session.get('correo', None)

    peticionesRol = Peticiones.objects.filter(tipoPeticion="Cambio de rol")
    peticionesGeneral = Peticiones.objects.exclude(tipoPeticion="Cambio de rol")

    contexto = {'rol': rol, 'correo': correo, 'peticionesRol': peticionesRol, 'peticionesGeneral': peticionesGeneral}
    return render (request,'core/admin/verPeticiones.html', contexto)

def mostrarVerPeticion(request):
    rol = request.session.get('rol', None)
    correo = request.session.get('correo', None)

    contexto = {'rol': rol, 'correo': correo}

    return render (request,'core/admin/verPeticion.html', contexto)

