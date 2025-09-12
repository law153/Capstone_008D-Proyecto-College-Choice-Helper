from django.shortcuts import render


# Instituciones
def mostrarRegistroInstitucion(request):
    return render(request, 'core/institucion/agregarInstitucion.html')

def mostrarEditarInstitucion(request):
    return render(request, 'core/institucion/editarInstitucion.html')
