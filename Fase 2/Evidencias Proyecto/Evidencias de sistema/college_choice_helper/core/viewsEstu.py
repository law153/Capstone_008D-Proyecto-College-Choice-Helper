from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Usuario, Rol, Peticiones, Institucion, Parametros, Carrera

# Estudiantes
def mostrarFormularioEstudiante(request):
    rol = request.session.get('rol', None)

    contexto = {'rol': rol}
    return render(request, 'core/estudiantes/formularioEstudiante.html', contexto)

def mostrarRecomendaciones(request):
    rol = request.session.get('rol', None)

    contexto = {'rol': rol}
    return render(request, 'core/estudiantes/recomendaciones.html', contexto)

def mostrarVistaInstituciones(request):
    rol = request.session.get('rol', None)

    contexto = {'rol': rol}
    return render(request, 'core/estudiantes/vistaInstitucion.html', contexto)

def mostrarCambioClave(request):
    rol = request.session.get('rol', None)

    contexto = {'rol': rol}
    return render(request, 'core/estudiantes/cambiarClave.html', contexto)

def mostrarCambioCorreo(request):
    rol = request.session.get('rol', None)

    contexto = {'rol': rol}
    return render(request, 'core/estudiantes/cambiarCorreo.html', contexto)

def mostrarGestionCuenta(request):
    rol = request.session.get('rol', None)

    contexto = {'rol': rol}
    return render(request, 'core/estudiantes/gestionCuenta.html', contexto)

def mostrarHacerPeticion(request):
    rol = request.session.get('rol', None)

    contexto = {'rol': rol}
    return render(request, 'core/estudiantes/hacerPeticion.html', contexto)

def cierreSesion(request):
    logout(request)
    return redirect('mostrarIndex')

def generarPeticion(request):
    if request.method == 'POST':
        correo = request.session.get('correo', None)
        usuario = Usuario.objects.get(correo=correo)

        asunto = request.POST.get('asunto')
        tipoPeticion = request.POST.get('tipo')
        mensaje = request.POST.get('mensaje')

        Peticiones.objects.create(asunto = asunto, tipoPeticion = tipoPeticion, mensaje = mensaje, usuario = usuario)
        print("Petición creada con éxito")
        return redirect('mostrarHacerpeticion')

    else:
        print("Petición fallada :,c", asunto, tipoPeticion, mensaje, correo)
        return redirect('mostrarHacerpeticion')



