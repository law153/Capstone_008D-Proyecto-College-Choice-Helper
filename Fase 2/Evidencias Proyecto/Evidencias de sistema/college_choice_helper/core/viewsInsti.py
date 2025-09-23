from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from .models import Institucion, Usuario


# Instituciones
def mostrarRegistroInstitucion(request):
    if request.user.is_authenticated:
        return render(request, 'core/institucion/agregarInstitucion.html')
    else:
        print("Debe iniciar sesión para acceder a este contenido")
        return redirect('mostrarLogin')

def mostrarEditarInstitucion(request):
    if request.user.is_authenticated:
        return render(request, 'core/institucion/editarInstitucion.html')
    else:
        print("Debe iniciar sesión para acceder a este contenido")
        return redirect('mostrarLogin')

def insertarInsti(request):
    nombreI = request.POST['nombre_insti']
    comunaI = request.POST['comuna_insti']
    esUniversidadI = request.POST['es_uni']
    gratuidadI = request.POST['gratuidad']
    aniosAcreditacionI = request.POST['anios_acreditacion']
    webInstiI = request.POST['web_insti']

    username = request.session.get('correo')
    tomarIdUser = Usuario.objects.get(correo=username)
    
    existeInsti = Institucion.objects.filter(
        nombreInstitucion = nombreI,
        comunaInstitucion = comunaI
    ).first()

    confirmarUni = True if esUniversidadI == "True" else False
    
    confirmarGratuidad = True if gratuidadI == "True" else False

    if existeInsti:
        print("Ya existe una institucion con el mismo nombre y comuna")
        return redirect('agregar_institucion')
    else:
        Institucion.objects.create(
            nombreInstitucion = nombreI,
            comunaInstitucion = comunaI,
            esUniversidadInsti = confirmarUni,
            webInstitucion = webInstiI,
            adscritoGratuidad = confirmarGratuidad,
            acreditacion = aniosAcreditacionI,
            usuario = tomarIdUser
        )
        print("La institución fue agregada correctamente")
        return redirect('agregar_institucion')
