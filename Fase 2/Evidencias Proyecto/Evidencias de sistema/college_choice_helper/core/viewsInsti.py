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

def mostrarEditarInstitucion(request,id_insti):
    if request.user.is_authenticated:
        institucion = Institucion.objects.get(idInstitucion = id_insti)
        print("nombre institucion", institucion.nombreInstitucion)

        contexto = {
            "institution" : institucion
        }
        return render(request, 'core/institucion/editarInstitucion.html',contexto)
    else:
        print("Debe iniciar sesión para acceder a este contenido")
        return redirect('mostrarLogin')

def insertarInsti(request):
    if request.user.is_authenticated:
        nombreI = request.POST['nombre_insti']
        comunaI = request.POST['comuna_insti']
        esUniversidadI = request.POST['es_uni']
        gratuidadI = request.POST['gratuidad']
        aniosAcreditacionI = request.POST['anios_acreditacion']
        webInstiI = request.POST['web_insti']
        fotoI = request.FILES['foto_insti']

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
            return redirect('mostrarRegistroInstitucion')
        else:
            Institucion.objects.create(
                nombreInstitucion = nombreI,
                comunaInstitucion = comunaI,
                esUniversidadInsti = confirmarUni,
                webInstitucion = webInstiI,
                adscritoGratuidad = confirmarGratuidad,
                acreditacion = aniosAcreditacionI,
                fotoInstitucion = fotoI,
                usuario = tomarIdUser
            )
            print("La institución fue agregada correctamente")
            return redirect('mostrarIndex')
    else:
        print("Debe iniciar sesión para acceder a este contenido")
        return redirect('mostrarLogin')

def actualizarInsti(request):
    if request.user.is_authenticated:
        idI = request.POST['id_insti']
        nombreI = request.POST['nombre_insti']
        comunaI = request.POST['comuna_insti']
        esUniversidadI = request.POST['es_uni']
        gratuidadI = request.POST['gratuidad']
        aniosAcreditacionI = request.POST['anios_acreditacion']
        webInstiI = request.POST['web_insti']
        fotoI = request.FILES.get('foto_insti', institucion.fotoInstitucion)

        username = request.session.get('correo')
        tomarIdUser = Usuario.objects.get(correo=username)

        confirmarUni = True if esUniversidadI == "True" else False
        confirmarGratuidad = True if gratuidadI == "True" else False

        institucion = Institucion.objects.get(idInstitucion = idI).first()

        existeInsti = Institucion.objects.filter(
            nombreInstitucion = nombreI
        ).first()

        if existeInsti:
            print("Ya hay una institución con el mismo nombre")
            return redirect('mostrarEditarInstitucion')
        else:
            institucion.nombreInstitucion = nombreI,
            institucion.comunaInstitucion = comunaI,
            institucion.esUniversidadInsti = esUniversidadI,
            institucion.adscritoGratuidad = gratuidadI,
            institucion.acreditacion = aniosAcreditacionI,
            institucion.webInstitucion = webInstiI,
            institucion.fotoInstitucion = fotoI
            institucion.usuario = tomarIdUser
            institucion.save()
            print("La institución se edito correctamente")
            return redirect('mostrarIndex')
    else:
        print("Debe iniciar sesión para acceder a este contenido")
    return redirect('mostrarLogin')