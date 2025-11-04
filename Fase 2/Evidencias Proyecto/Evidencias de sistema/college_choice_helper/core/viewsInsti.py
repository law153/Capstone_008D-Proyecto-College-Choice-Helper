from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login, logout
from .models import Institucion, Usuario, Carrera
import re
import unicodedata
from django.contrib import messages
import requests
import json
import os
from django.conf import settings

# Instituciones
def mostrarRegistroInstitucion(request):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)
        if rol != 1:
            messages.warning(request,'No tiene rol de gestor institucional!')
            return redirect('mostrarIndex')
        
        acreditaciones = [0,1,2,3,4,5,6,7]
        comunas = obtener_comunas_metropolitana()
        contexto = {'rol': rol, 'acreditaciones': acreditaciones, 'comunas': comunas}


        return render(request, 'core/institucion/agregarInstitucion.html', contexto)
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')
    
def mostrarListadoInstitucion(request):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)
        if rol != 1:
            messages.warning(request,'No tiene rol de gestor institucional!')
            return redirect('mostrarIndex')
        correo = request.session.get('correo', None)
        usuario1 = Usuario.objects.get(correo=correo)
        instituciones = Institucion.objects.filter(usuario=usuario1)
        contexto = {'rol': rol, 'instituciones': instituciones}


        return render(request, 'core/institucion/listadoInstituciones.html', contexto)
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')
    
def mostrarListadoCarreras(request, id_insti):
    if request.user.is_authenticated == False:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')
    
    rol = request.session.get('rol', None)
    if rol != 1:
        messages.warning(request,'No tiene rol de gestor institucional!')
        return redirect('mostrarIndex')

    
    
    institucion = Institucion.objects.get(idInstitucion=id_insti)

    carreras = Carrera.objects.filter(institucion=institucion)
    contexto = {'rol': rol,  'carreras': carreras, 'insti': institucion}

    return render(request, 'core/institucion/verCarreras.html', contexto)

def mostrarAgregarCarrera(request, id_insti):
    if request.user.is_authenticated == False:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')
    
    rol = request.session.get('rol', None)

    if rol != 1:
        messages.warning(request,'No tiene rol de gestor institucional!')
        return redirect('mostrarIndex')
    
    institucion = Institucion.objects.get(idInstitucion=id_insti)

    contexto = {'rol': rol, 'insti': institucion}

    return render(request, 'core/institucion/agregarCarrera.html', contexto)

def mostrarEditarCarrera(request, id_carrera, id_insti):
    if request.user.is_authenticated == False:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')
    
    rol = request.session.get('rol', None)

    if rol != 1:
        messages.warning(request,'No tiene rol de gestor institucional!')
        return redirect('mostrarIndex')
    
    institucion = Institucion.objects.get(idInstitucion=id_insti)

    carrera = Carrera.objects.get(idCarrera=id_carrera)
    comunas = obtener_comunas_metropolitana()
    contexto = {'rol': rol, 'insti': institucion, 'carrera': carrera}

    return render(request, 'core/institucion/editarCarrera.html', contexto)

def mostrarEditarInstitucion(request, id_insti):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)
        if rol != 1:
            messages.warning(request,'No tiene rol de gestor institucional!')
            return redirect('mostrarIndex')
        institucion = Institucion.objects.get(idInstitucion = id_insti)
        acreditaciones = [0,1,2,3,4,5,6,7]
        comunas = obtener_comunas_metropolitana()
        contexto = {
            "insti" : institucion,
            'rol': rol,
            'acreditaciones': acreditaciones,
            'comunas': comunas
        }
        return render(request, 'core/institucion/editarInstitucion.html', contexto)
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')

def insertarInsti(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            nombreI = request.POST['nombre_insti']
            comunaI = request.POST['comuna_insti']
            gratuidadI = request.POST['gratuidad']
            aniosAcreditacionI = request.POST['anios_acreditacion']
            webInstiI = request.POST['web_insti']
            fotoI = request.FILES.get('foto_insti')
            tipoInsti = request.POST['tipoInsti']


            username = request.session.get('correo')
            tomarIdUser = Usuario.objects.get(correo=username)
            
            existeInsti = Institucion.objects.filter(
                nombreInstitucion = nombreI,
                comunaInstitucion = comunaI
            ).first()

            
            
            confirmarGratuidad = True if gratuidadI == "True" else False

            if fotoI == None:
                fotoI = 'default_insti.png'
            
            if existeInsti:
                messages.error(request,"Ya existe una institucion con el mismo nombre y comuna")
                return redirect('mostrarRegistroInstitucion')
            else:
                Institucion.objects.create(
                    nombreInstitucion = nombreI,
                    comunaInstitucion = comunaI,
                    webInstitucion = webInstiI,
                    adscritoGratuidad = confirmarGratuidad,
                    acreditacion = aniosAcreditacionI,
                    fotoInstitucion = fotoI,
                    tipoInstitucion = tipoInsti,
                    usuario = tomarIdUser
                )
                messages.success(request,"La institución fue agregada correctamente")
                return redirect('mostrarIndex')
        else:
            messages.warning(request,'Algo salío mal')
            return redirect('mostrarRegistroInstitucion')
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')

def actualizarInsti(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            idI = request.POST['id_insti']
            nombreI = request.POST['nombre_insti']
            comunaI = request.POST['comuna_insti']
            gratuidadI = request.POST['gratuidad']
            aniosAcreditacionI = request.POST['anios_acreditacion']
            webInstiI = request.POST['web_insti']
            tipoInsti = request.POST['tipoInsti']
            print(tipoInsti)
            #username = request.session.get('correo')
            #tomarIdUser = Usuario.objects.get(correo=username)

            
            confirmarGratuidad = True if gratuidadI == "True" else False

            institucion = Institucion.objects.get(idInstitucion = idI)
            fotoI = request.FILES.get('foto_insti', institucion.fotoInstitucion)
            
            if Institucion.objects.filter(nombreInstitucion=nombreI.strip()).exclude(idInstitucion=idI).exists():
                messages.error(request,"Ya hay una institución con el mismo nombre")
                return redirect('mostrarEditarInstitucion', idI)
            else:

                institucion.nombreInstitucion = nombreI
                institucion.comunaInstitucion = comunaI
                institucion.adscritoGratuidad = confirmarGratuidad
                institucion.acreditacion = aniosAcreditacionI
                institucion.webInstitucion = webInstiI
                institucion.fotoInstitucion = fotoI
                institucion.tipoInstitucion = tipoInsti
                #institucion.usuario = tomarIdUser
                institucion.save()
                messages.success(request,"La institución se editó correctamente")
                return redirect('mostrarIndex')
        else:
            messages.warning(request,'Algo salío mal')
            return('mostrarEditarInstitucion')
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
    return redirect('mostrarLogin')

def eliminarInsti(request, id_insti):
    if request.user.is_authenticated:
        if request.method == 'POST':
            institucion = Institucion.objects.get(idInstitucion = id_insti)
            institucion.delete()
            messages.success(request,"Se eliminó la institución")
            return redirect('mostrarIndex')
        else:
            messages.warning(request,'Algo salío mal')
            return("mostrarEditarInstitucion")
    else:
        messages.warning(request,'Debes iniciar sesión para acceder a este contenido!')
        return redirect('mostrarLogin')
    
def agregarCarrera(request, id_insti):
    if request.user.is_authenticated == False:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')
    
    rol = request.session.get('rol', None)

    if rol != 1:
        messages.warning(request,'No tiene rol de gestor institucional!')
        return redirect('mostrarIndex')
    
    
    institucion = Institucion.objects.get(idInstitucion=id_insti)
    if request.method == 'POST':
        nombre = request.POST.get('nombre_carrera', None)
        puntaje = request.POST.get('puntaje', None)
        costo = request.POST.get('costo', None)

        if nombre:
            nombre = normalizar_nombre(nombre)


        control = False #Si False todo bien, si True hay un error
        errores = []

        if not nombre or nombre.strip() == "":
            errores.append("El nombre de la carrera no puede estar vacío.")
            control = True
        if not puntaje or not puntaje.isdigit() or int(puntaje) < 0:
            errores.append("El puntaje mínimo debe ser un número entero positivo.")
            control = True

        if not costo or not costo.isdigit() or int(costo) < 0:
            errores.append("El costo debe ser un número entero positivo.")
            control = True

        if Carrera.objects.filter(nombreCarrera=nombre.strip(), institucion=institucion).exists():
            errores.append("Ya existe una carrera con este nombre en la institución.")
            control = True


        if control:
            for error in errores:
                messages.error(request,"Error: "+ error)
            return redirect('mostrarAgregarCarrera', id_insti=id_insti)
        
        puntaje = int(puntaje)
        costo = int(costo)

        Carrera.objects.create(nombreCarrera = nombre, puntajeMinimo = puntaje, costo = costo, institucion = institucion)
        messages.success(request,"La carrera fue agregada correctamente")
        return redirect('mostrarListadoCarreras', id_insti=id_insti)


    else:
        messages.warning(request,'Algo salío mal')
        return redirect('mostrarAgregarCarrera', id_insti=id_insti)

def editarCarrera(request, id_carrera, id_insti):
    if request.user.is_authenticated == False:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')
    
    rol = request.session.get('rol', None)

    if rol != 1:
        messages.warning(request,'No tiene rol de gestor institucional!')
        return redirect('mostrarIndex')
    
    institucion = get_object_or_404(Institucion, idInstitucion=id_insti)
    
    carrera = get_object_or_404(Carrera, idCarrera=id_carrera)
    if request.method == 'POST':
        nombre = request.POST.get('nombre_carrera', None)
        puntaje = request.POST.get('puntaje', None)
        costo = request.POST.get('costo', None)

        if nombre:
            nombre = normalizar_nombre(nombre)


        control = False #Si False todo bien, si True hay un error
        errores = []

        if not nombre or nombre.strip() == "":
            errores.append("El nombre de la carrera no puede estar vacío.")
            control = True
        if not puntaje or not puntaje.isdigit() or int(puntaje) < 0:
            errores.append("El puntaje mínimo debe ser un número entero positivo.")
            control = True

        if not costo or not costo.isdigit() or int(costo) < 0:
            errores.append("El costo debe ser un número entero positivo.")
            control = True

        if Carrera.objects.filter(nombreCarrera=nombre.strip(), institucion=institucion).exclude(idCarrera=carrera.idCarrera).exists():
            errores.append("Ya existe una carrera con este nombre en la institución.")
            control = True


        if control:
            for error in errores:
                messages.error(request,"Error: "+ error)
            return redirect('mostrarEditarCarrera', id_carrera=id_carrera, id_insti=id_insti)
        
        puntaje = int(puntaje)
        costo = int(costo)

        carrera.nombreCarrera = nombre
        carrera.puntajeMinimo = puntaje
        carrera.costo = costo
        carrera.save()
        messages.success(request,"La carrera fue editada correctamente")
        return redirect('mostrarListadoCarreras', id_insti=id_insti)
    
def eliminarCarrera(request, id_carrera, id_insti):
    if request.user.is_authenticated == False:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')
    
    rol = request.session.get('rol', None)

    if rol != 1:
        messages.warning(request,'No tiene rol de gestor institucional!')
        return redirect('mostrarIndex')
    
    if request.method == 'POST':
        carrera = get_object_or_404(Carrera, idCarrera=id_carrera)
        id_insti = carrera.institucion.idInstitucion
        carrera.delete()
        messages.success(request,"La carrera fue eliminada correctamente")
        return redirect('mostrarListadoCarreras', id_insti=id_insti)
    else:
        messages.warning(request,'Algo salío mal')
        return redirect('mostrarListadoCarreras', id_insti=id_insti)




def normalizar_nombre(nombre: str) -> str:
    # 1. Eliminar espacios al inicio y final
    nombre = nombre.strip()

    # 2. Reemplazar múltiples espacios por uno solo
    nombre = re.sub(r'\s+', ' ', nombre)

    # 3. Quitar tildes
    nombre = ''.join(
        c for c in unicodedata.normalize('NFD', nombre)
        if unicodedata.category(c) != 'Mn'
    )

    # 4. Primera letra mayúscula, resto minúsculas
    nombre = nombre.capitalize()

    return nombre

def obtener_comunas_metropolitana():
    try:
        # Ruta absoluta al archivo JSON
        ruta_json = os.path.join(settings.BASE_DIR, 'core', 'static', 'core', 'data', 'comunas-regiones.json')

        # Leer el archivo
        with open(ruta_json, 'r', encoding='utf-8') as archivo:
            data = json.load(archivo)

        # Buscar la región metropolitana
        for region_data in data.get("regiones", []):
            if region_data["region"].lower().strip() == "región metropolitana de santiago":
                return region_data["comunas"]

        return []  # Si no se encuentra la región
    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo comunas-regiones.json")
        return []
    except json.JSONDecodeError:
        print("❌ Error: El archivo comunas-regiones.json no tiene un formato JSON válido")
        return []
    except Exception as e:
        print(f"❌ Error al leer comunas: {e}")
        return []
