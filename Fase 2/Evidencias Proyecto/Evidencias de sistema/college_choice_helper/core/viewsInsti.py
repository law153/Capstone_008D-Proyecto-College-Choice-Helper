from django.shortcuts import render, redirect
from .models import Institucion


# Instituciones
def mostrarRegistroInstitucion(request):
    return render(request, 'core/institucion/agregarInstitucion.html')

def mostrarEditarInstitucion(request):
    return render(request, 'core/institucion/editarInstitucion.html')

def insertarInsti(request):
    nombreI = request.post['nombre_insti']
    comunaI = request.post['comuna_insti']
    esUniversidadI = request.post['es_uni']
    gratuidadI = request.post['gratuidad']
    aniosAcreditacionI = request.post['anios_acreditacion']
    webInstiI = request.post['webInsti']
    
    existeInsti = Institucion.objects.filter(
        nombreInstitucion = nombreI,
        comunaInstitucion = comunaI
    ).first()

    confirmarUni = True if esUniversidadI == "True" else False
    
    confirmarGratuidad = True if gratuidadI == "True" else False

    if existeInsti:
        print("Ya existe una institucion con el mismo nombre y comuna")
        return redirect('mostrarRegistroInstitucion')
    else:
        Institucion.objects.create(
            nombreInstitucion = nombreI,
            comunaInstitucion = comunaI,
            esUniversidadInsti = confirmarUni,
            webInstitucion = webInstiI,
            adscritoGratuidad = confirmarGratuidad,
            acreditacion = aniosAcreditacionI
        )
        print("La institución fue agregada correctamente")
        return redirect('mostrarRegistroInstitucion')
