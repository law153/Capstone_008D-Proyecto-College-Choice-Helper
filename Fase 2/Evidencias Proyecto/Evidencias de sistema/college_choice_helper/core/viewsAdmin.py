from django.shortcuts import render, redirect
from .models import Usuario, Rol, Peticiones, Institucion, Parametros, Carrera
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q,  Count, Sum, Case, When, IntegerField
from collections import Counter
from django.db.models.functions import TruncMonth

#Admin
def mostrarGestionUsuarios(request):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)
        correo = request.session.get('correo', None)

        if rol != 2:
            messages.warning(request,'No tiene rol de administrador!')
            return redirect('mostrarIndex')

        rolEstu = Rol.objects.get(id_rol = 0)
        rolInsti = Rol.objects.get(id_rol = 1)

        estudiantes = Usuario.objects.filter(rol = rolEstu)
        institucionales = Usuario.objects.filter(rol = rolInsti)

        contexto = {
            'rol': rol,
            'correo': correo,
            'estu': estudiantes,
            'insti': institucionales     
        }
        return render (request,'core/admin/gestionUsuarios.html', contexto)
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')

def mostrarGestionInsti(request):
    if request.user.is_authenticated == False:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')

    rol = request.session.get('rol', None)

    if rol != 2:
            messages.warning(request,'No tiene rol de administrador!')
            return redirect('mostrarIndex')
    
    correo = request.session.get('correo', None)
 
    instituciones = Institucion.objects.all()

    contexto = {'rol': rol,
                'correo': correo,
                'insti': instituciones
    }
    return render (request,'core/admin/gestionInstituciones.html', contexto)

def mostrarEstadisticas(request):
    if request.user.is_authenticated == False:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')

    rol = request.session.get('rol', None)

    if rol != 2:
            messages.warning(request,'No tiene rol de administrador!')
            return redirect('mostrarIndex')
    
    estudiantes = Usuario.objects.filter(rol = 0)
    institucionales = Usuario.objects.filter(rol = 1)
    instituciones = Institucion.objects.all()
    parametros = Parametros.objects.filter(idParametros__rol=0)
    carrera = Carrera.objects.all()
    
    usuariosEliminados = Usuario.all_objects.filter(activo=False)

    #Estadisticas
    cantidadEstudiante = estudiantes.count()
    cantidadInstitucional = institucionales.count()
    cantidadInstituciones = instituciones.count()
    cantidadCarreras = carrera.count()
    cantidadUsuariosEliminados = usuariosEliminados.count()
    totalUsuarios = cantidadEstudiante + cantidadInstitucional

    comunas = [estu.comunaUsuario for estu in estudiantes]
    top_comunas_raw = Counter(comunas).most_common(3)
    top_comunas = [{"nombre": c[0], "cantidad": c[1]} for c in top_comunas_raw]
    
    carreras = [param.carrera for param in parametros]
    top_carreras_raw = Counter(carreras).most_common(3)
    top_carreras = [{"nombre": c[0], "cantidad": c[1]} for c in top_carreras_raw]

    tipoInsti = [insti.tipoInstitucion for insti in instituciones]
    top_tipoInsti_raw = Counter(tipoInsti).most_common(3)
    top_tipoInsti = [{"nombre": c[0], "cantidad": c[1]} for c in top_tipoInsti_raw]

    usuarios_por_mes = (User.objects.annotate(mes=TruncMonth('date_joined')).values('mes').annotate(total=Count('id')).order_by('mes'))



    FLAGS = [
        'comunaRelevancia',
        'budgetRelevancia',
        'gratuidadRelevancia',
        'acreditacionRelevancia',
        'esUniversidadRelevancia',
        'puntajeNemRelevancia',
        'carreraRelevancia',
    ]

    aggs = {'total_estudiantes': Count('pk')}
    for f in FLAGS:
        aggs[f] = Sum(
            Case(When(**{f: True}, then=1), default=0, output_field=IntegerField())
        )

    res = parametros.aggregate(**aggs)

    total_estudiantes = res['total_estudiantes'] or 0
    total_trues = sum((res[f] or 0) for f in FLAGS)

    
    promedio_param_activados = round(total_trues / total_estudiantes, 2) if total_estudiantes else 0.0
    
    print(promedio_param_activados)

    stats = [
        {"nombre": "Usuarios estudiantiles registrados", "valor": cantidadEstudiante},
        {"nombre": "Usuarios institucionales registrados", "valor": cantidadInstitucional},
        
    ]


    contexto = {'rol': rol,
                'estadisticas': stats,
                'top_comunas': top_comunas,
                'top_carreras': top_carreras,
                'top_tipoInsti': top_tipoInsti,
                'usuarios_por_mes': usuarios_por_mes,
                'cantidadInstituciones': cantidadInstituciones,
                'totalUsuarios': totalUsuarios,
                'cantidadCarreras': cantidadCarreras,
                'promedio_param_activados': promedio_param_activados,
                'cantidadUsuariosEliminados': cantidadUsuariosEliminados,}

    return render (request,'core/admin/estadisticasAdmin.html', contexto)

def mostrarVerPeticiones(request):
    rol = request.session.get('rol', None)

    if rol != 2: 
            messages.warning(request,'No tiene rol de administrador!')
            return redirect('mostrarIndex')
    
    correo = request.session.get('correo', None)

    peticionesRol = Peticiones.objects.filter( ~Q(estadoPeticion="Revisada"), tipoPeticion="Cambio de rol" )
    peticionesGeneral = Peticiones.objects.filter(
        ~Q(tipoPeticion="Cambio de rol"),
        ~Q(estadoPeticion="Revisada")  
    )
    peticionesRevisadas = Peticiones.objects.filter(estadoPeticion = "Revisada")


    contexto = {'rol': rol, 'correo': correo, 'peticionesRol': peticionesRol, 'peticionesGeneral': peticionesGeneral, 'peticionesRevisadas' : peticionesRevisadas}
    return render (request,'core/admin/verPeticiones.html', contexto)

def mostrarVerPeticion(request, idPeticiones):
    rol = request.session.get('rol', None)

    if rol != 2:
            messages.warning(request,'No tiene rol de administrador!')
            return redirect('mostrarIndex')
    
    correo = request.session.get('correo', None)

    peticion = Peticiones.objects.get(idPeticiones=idPeticiones)

    contexto = {'rol': rol, 'correo': correo, 'peticion': peticion}

    return render(request,'core/admin/verPeticion.html', contexto)

def cambiarRol(request, idPeticion, correo):
    if request.method == 'POST':
        
        cambio = request.POST.get('toggleCambio', None)
        if cambio == 'on':
            usuario = Usuario.objects.get(correo=correo)
            registroRol = Rol.objects.get(id_rol=1) #1 para institución
            usuario.rol = registroRol
            usuario.save()
            peticion = Peticiones.objects.get(idPeticiones=idPeticion)
            peticion.estadoPeticion = "Revisada"
            peticion.save()
            messages.warning(request,'Se cambio exitosamente el rol a: Gestor institucional')
            return redirect('mostrarVerPeticiones')
        else:
            peticion = Peticiones.objects.get(idPeticiones=idPeticion)
            peticion.estadoPeticion = "Revisada"
            peticion.save()
            messages.success(request,'No se cambio el rol al usuario.')
            return redirect('mostrarVerPeticiones')
    else:
        return redirect('mostrarVerPeticion', idPeticion)
    
def eliminarUsuarioAdm(request, correoU):
    if request.user.is_authenticated == False:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')
    
    if request.method == 'POST':
        usuario = Usuario.objects.get(correo = correoU)
        
        if usuario.rol.id_rol == 2:
            messages.warning(request, "No puedes eliminar otro administrador.")
            return redirect('mostrarGestionUsuarios')

        user = User.objects.get(username = usuario.correo)
        usuario.delete()
        user.is_active = False
        user.save()
        messages.success(request,"Se eliminó el usuario")
        return redirect('mostrarIndex')
    
def eliminarInstiAdm(request, id_insti):
    if request.user.is_authenticated == False:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')
    if request.method == 'POST':
        insti = Institucion.objects.get(idInstitucion = id_insti)
        insti.delete()
        messages.success(request,"Se eliminó la institución")
        return redirect('mostrarIndex')
    

def revisarPeticion(request, idPeticion):
    rol = request.session.get('rol', None)

    if rol != 2:
            messages.warning(request,'No tiene rol de administrador!')
            return redirect('mostrarIndex')
    if request.method == 'POST':
         peticion = Peticiones.objects.get(idPeticiones=idPeticion)

         peticion.estadoPeticion = "Revisada"
         peticion.save()
         messages.success(request,"La petición se marcó como revisada!")

         return redirect('mostrarIndex')

     


