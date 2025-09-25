from django.shortcuts import render, redirect
from django.contrib.auth import logout

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



