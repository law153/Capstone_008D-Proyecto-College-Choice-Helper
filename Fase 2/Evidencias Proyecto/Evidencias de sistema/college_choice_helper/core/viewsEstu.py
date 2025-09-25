from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Estudiantes
def mostrarFormularioEstudiante(request):
    return render(request, 'core/estudiantes/formularioEstudiante.html')

def mostrarRecomendaciones(request):
    return render(request, 'core/estudiantes/recomendaciones.html')

def mostrarVistaInstituciones(request):
    return render(request, 'core/estudiantes/vistaInstitucion.html')

def mostrarCambioClave(request):
    return render(request, 'core/estudiantes/cambiarClave.html')

def mostrarCambioCorreo(request):
    return render(request, 'core/estudiantes/cambiarCorreo.html')

def mostrarGestionCuenta(request):
    return render(request, 'core/estudiantes/gestionCuenta.html')

def mostrarHacerPeticion(request):
    return render(request, 'core/estudiantes/hacerPeticion.html')

def cierreSesion(request):
    logout(request)
    return redirect('mostrarIndex')



