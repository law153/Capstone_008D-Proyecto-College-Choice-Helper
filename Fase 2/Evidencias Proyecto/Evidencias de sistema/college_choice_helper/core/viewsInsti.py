from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from .models import Institucion, Usuario


# Instituciones
def mostrarRegistroInstitucion(request):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)

        contexto = {'rol': rol}


        return render(request, 'core/institucion/agregarInstitucion.html', contexto)
    else:
        print("Debe iniciar sesión para acceder a este contenido")
        return redirect('mostrarLogin')

def mostrarEditarInstitucion(request,id_insti):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)
        institucion = Institucion.objects.get(idInstitucion = id_insti)
        print("nombre institucion", institucion.nombreInstitucion)

        contexto = {
            "institution" : institucion,
            'rol': rol
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
        

        username = request.session.get('correo')
        tomarIdUser = Usuario.objects.get(correo=username)

        confirmarUni = True if esUniversidadI == "True" else False
        confirmarGratuidad = True if gratuidadI == "True" else False

        institucion = Institucion.objects.get(idInstitucion = idI)
        fotoI = request.FILES.get('foto_insti', institucion.fotoInstitucion)

        existeInsti = Institucion.objects.filter(
            nombreInstitucion = nombreI
        ).first()

        if existeInsti:
            print("Ya hay una institución con el mismo nombre")
            return redirect('mostrarEditarInstitucion')
        else:
            # 🔎 PRINTS DE DEBUG
            print("DEBUG nombreI:", nombreI)
            print("DEBUG comunaI:", comunaI)
            print("DEBUG confirmarUni:", confirmarUni)
            print("DEBUG confirmarGratuidad:", confirmarGratuidad)
            print("DEBUG aniosAcreditacionI:", aniosAcreditacionI)
            print("DEBUG webInstiI:", webInstiI)
            print("DEBUG fotoI:", fotoI)
            print("DEBUG tipo fotoI:", type(fotoI))

            institucion.nombreInstitucion = nombreI
            institucion.comunaInstitucion = comunaI
            institucion.esUniversidadInsti = confirmarUni
            institucion.adscritoGratuidad = confirmarGratuidad
            institucion.acreditacion = aniosAcreditacionI
            institucion.webInstitucion = webInstiI
            institucion.fotoInstitucion = fotoI
            institucion.usuario = tomarIdUser
            institucion.save()
            print("La institución se edito correctamente")
            return redirect('mostrarIndex')
    else:
        print("Debe iniciar sesión para acceder a este contenido")
    return redirect('mostrarLogin')