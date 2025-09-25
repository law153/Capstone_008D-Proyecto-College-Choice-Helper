from django.shortcuts import render, redirect
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

