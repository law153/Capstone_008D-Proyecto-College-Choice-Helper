from django.shortcuts import render

# Estudiantes
def mostrarFormularioEstudiante(request):
    return render(request, 'core/estudiantes/formularioEstudiante.html')

def mostrarRecomendaciones(request):
    return render(request, 'core/estudiantes/recomendaciones.html')

def mostrarVistaInstituciones(request):
    return render(request, 'core/estudiantes/vistaInstitucion.html')

