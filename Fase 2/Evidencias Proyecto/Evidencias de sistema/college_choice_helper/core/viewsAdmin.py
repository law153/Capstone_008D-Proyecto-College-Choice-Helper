from django.shortcuts import render, redirect
from .models import Usuario, Rol, Peticiones, Institucion
from django.db import transaction
from django.contrib.auth.models import User

#Admin
def mostrarGestionUsuarios(request):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)
        correo = request.session.get('correo', None)

        rolEstu = Rol.objects.get(id_rol = 0)
        rolInsti = Rol.objects.get(id_rol = 1)

        estudiantes = Usuario.objects.filter(rol = rolEstu)
        institucionales = Usuario.objects.filter(rol = rolInsti)

        contexto = {
            'rol': rol,
            'correo': correo,
            'estu': estudiantes,
            'insti': institucionales     
        }
        return render (request,'core/admin/gestionUsuarios.html', contexto)
    else:
        print("Debe iniciar sesión para acceder a este contenido")
        return redirect('mostrarLogin')

def mostrarGestionInsti(request):
    if request.user.is_authenticated == False:
        print("Debe iniciar sesión para acceder a este contenido")
        return redirect('mostrarLogin')

    rol = request.session.get('rol', None)
    correo = request.session.get('correo', None)
 
    instituciones = Institucion.objects.all()

    contexto = {'rol': rol,
                'correo': correo,
                'insti': instituciones
    }
    return render (request,'core/admin/gestionInstituciones.html', contexto)

def mostrarVerPeticiones(request):
    rol = request.session.get('rol', None)
    correo = request.session.get('correo', None)

    peticionesRol = Peticiones.objects.filter(tipoPeticion="Cambio de rol")
    peticionesGeneral = Peticiones.objects.exclude(tipoPeticion="Cambio de rol")

    contexto = {'rol': rol, 'correo': correo, 'peticionesRol': peticionesRol, 'peticionesGeneral': peticionesGeneral}
    return render (request,'core/admin/verPeticiones.html', contexto)

def mostrarVerPeticion(request, idPeticiones):
    rol = request.session.get('rol', None)
    correo = request.session.get('correo', None)

    peticion = Peticiones.objects.get(idPeticiones=idPeticiones)

    contexto = {'rol': rol, 'correo': correo, 'peticion': peticion}

    return render(request,'core/admin/verPeticion.html', contexto)

def cambiarRol(request, idPeticion, correo):
    if request.method == 'POST':
        cambio = request.POST.get('toggleCambio', None)
        if cambio == 'on':
            usuario = Usuario.objects.get(correo=correo)
            registroRol = Rol.objects.get(id_rol=1) #1 para institución
            usuario.rol = registroRol
            usuario.save()
            print("Rol cambio con exito a: ",usuario.rol.nombre_rol)
            return redirect('mostrarVerPeticiones')
        else:
            return redirect('mostrarVerPeticion', idPeticion)
    else:
        return redirect('mostrarVerPeticion', idPeticion)
    
def eliminarUsuarioAdm(request, correoU):
    if request.user.is_authenticated == False:
        print("Debe iniciar sesión para acceder a este contenido")
        return redirect('mostrarLogin')
    
    if request.method == 'POST':
        usuario = Usuario.objects.get(correo = correoU)
        user = User.objects.get(username = usuario.correo)
        usuario.delete()
        user.delete()
        print("Se eliminó el usuario")
        return redirect('mostrarIndex')

