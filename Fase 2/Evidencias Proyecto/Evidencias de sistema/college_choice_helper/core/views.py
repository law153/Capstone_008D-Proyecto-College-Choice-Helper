from django.shortcuts import render

# Sin cuenta
def mostrarIndex(request):
    return render(request, 'core/index.html')

def mostrarLogin(request):
    return render(request, 'core/sinCuenta/login.html')

def mostrarRegistro(request):
    return render(request, 'core/sinCuenta/registrarse.html')


# Estudiantes
def mostrarFormularioEstudiante(request):
    return render(request, 'core/estudiantes/formularioEstudiante.html')

def mostrarRecomendaciones(request):
    return render(request, 'core/estudiantes/recomendaciones.html')

def mostrarVistaInstituciones(request):
    return render(request, 'core/estudiantes/vistaInstitucion.html')


# Instituciones

