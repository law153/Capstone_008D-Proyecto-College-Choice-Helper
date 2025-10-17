from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate
from .models import Usuario, Rol, Peticiones, Institucion, Parametros, Carrera
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import transaction
from django.contrib.auth.hashers import check_password
from django.contrib import messages
# Estudiantes
def mostrarFormularioEstudiante(request):
    if request.user.is_authenticated:
        
        rol = request.session.get('rol', None)

        if rol != 0:
            messages.warning(request,'No tiene rol estudiante!')
            return redirect('mostrarIndex')

        correo = request.session.get('correo', None)
        usuario1 = Usuario.objects.get(correo=correo)

        parametros = Parametros.objects.get(idParametros=usuario1)

        carreras = Carrera.objects.values_list('nombreCarrera', flat=True).distinct().order_by('nombreCarrera')

        comunas = Institucion.objects.values_list('comunaInstitucion', flat=True).distinct().order_by('comunaInstitucion') 

        acreditaciones = [0,1,2,3,4,5,6,7]


        contexto = {'rol': rol, 'parametros': parametros, 'carreras': carreras, 'comunas': comunas, 'acreditaciones': acreditaciones}

        return render(request, 'core/estudiantes/formularioEstudiante.html', contexto)
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')

def mostrarRecomendaciones(request):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)

        if rol != 0:
            messages.warning(request,'No tiene rol estudiante!')
            return redirect('mostrarIndex')
        correo = request.session.get('correo', None)
        usuario = Usuario.objects.get(correo=correo)
        parametros = Parametros.objects.get(idParametros=usuario)

        recomendaciones = generar_recomendaciones(usuario, parametros.esUniversidad)

        contexto = {'rol': rol, 'recomendaciones' : recomendaciones}
        return render(request, 'core/estudiantes/recomendaciones.html', contexto)
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')

def mostrarVistaInstituciones(request, id_insti):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)
        if rol != 0:
            messages.warning(request,'No tiene rol estudiante!')
            return redirect('mostrarIndex')
        
        institucion = Institucion.objects.get(idInstitucion = id_insti)
        carreras = Carrera.objects.filter(institucion = institucion)
        correo = request.session.get('correo',None)
        usuario =  Usuario.objects.get(correo=correo)
        score, porcen, detalles = calcular_score(usuario, id_insti)
        try:
            porcentaje = float(porcen) 
        except ValueError:
            porcentaje = 0
        contexto = {'rol': rol, 'institucion': institucion, 'carreras' : carreras, 'porcentaje': porcentaje, 'detalles': detalles}
        return render(request, 'core/estudiantes/vistaInstitucion.html', contexto)
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')
    

def mostrarCambioClave(request):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)


        contexto = {'rol': rol}
        return render(request, 'core/estudiantes/cambiarClave.html', contexto)
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')

def mostrarCambioCorreo(request):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)

        contexto = {'rol': rol}
        return render(request, 'core/estudiantes/cambiarCorreo.html', contexto)
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')

def mostrarGestionCuenta(request):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)

        contexto = {'rol': rol}
        return render(request, 'core/estudiantes/gestionCuenta.html', contexto)
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')

def mostrarHacerPeticion(request):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)

        contexto = {'rol': rol}
        return render(request, 'core/estudiantes/hacerPeticion.html', contexto)
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')
    
def mostrarEliminarCuenta(request):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)

        contexto = {'rol': rol}
        return render(request, 'core/estudiantes/eliminarCuenta.html', contexto)
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')

def cierreSesion(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('mostrarIndex')
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')

def generarPeticion(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            correo = request.session.get('correo', None)
            usuario = Usuario.objects.get(correo=correo)

            asunto = request.POST.get('asunto')
            tipoPeticion = request.POST.get('tipo')
            mensaje = request.POST.get('mensaje')

            if asunto and tipoPeticion and mensaje:
                Peticiones.objects.create(asunto = asunto, tipoPeticion = tipoPeticion, mensaje = mensaje, estadoPeticion= 'Pendiente',usuario = usuario)
                
                messages.success(request,'Petición creada con éxito!')
                return redirect('mostrarHacerpeticion')
            else:
                
                messages.error(request,'Los campos están vacíos!')
                return redirect('mostrarHacerpeticion')
        else:
            messages.warning(request,'Algo salio mal')
            return redirect('mostrarHacerpeticion')
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')
    

def cambiarCorreo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            correoActual = request.session.get('correo', None)
            clave = request.POST.get('clave', None)
            nuevoCorreo = request.POST.get('correo_new', None)
            repetirCorreo = request.POST.get('correo_rep', None)

            userAuth = authenticate(username = correoActual, password = clave)

            if userAuth is None:
                messages.error(request,'La contraseña ingresada no es correcta!')
                return redirect('mostrarCambioCorreo')
            
            if User.objects.filter(username=nuevoCorreo).exists():
                messages.error(request,'Ese correo ya esta en uso!')
                return redirect('mostrarCambioCorreo')
            
            try:
                validate_email(nuevoCorreo)
            except ValidationError:
                messages.error(request,'El correo ingresado no es valido!')
                return redirect('mostrarCambioCorreo')

            if nuevoCorreo != repetirCorreo:
                messages.error(request,'El correos no coinciden!')
                return redirect('mostrarCambioCorreo')
            
            with transaction.atomic():
                usuario = get_object_or_404(Usuario, correo=correoActual)
                usuario.correo = nuevoCorreo
                usuario.save()

                user = request.user
                user.username = nuevoCorreo
                user.email = nuevoCorreo
                user.save()

                logout(request)
                messages.success(request,'Correo cambiado con exito, por favor inicie sesión nuevamente')
                return redirect('mostrarLogin')
        
        else:
            messages.warning(request,'Algo salío mal')
            return redirect('mostrarCambioCorreo')
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')
    
def cambiarClave(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            correo = request.session.get('correo', None)
            clave = request.POST.get('clave', None)
            nuevaClave = request.POST.get('clave_new', None)
            repetirClave = request.POST.get('clave_rep', None)

            userAuth = authenticate(username = correo, password = clave)

            if userAuth is None:
                messages.error(request,'La contraseña ingresada no es correcta!')
                return redirect('mostrarCambioClave')
            
            if check_password(nuevaClave, request.user.password):
                messages.error(request,'Su nueva contraseña no puede ser igual a la actual!')
                return redirect('mostrarCambioClave')

            if nuevaClave != repetirClave:
                messages.error(request,'Las contraseñas no coinciden')
                return redirect('mostrarCambioClave')

            

            
            
            with transaction.atomic():
                user = request.user
                user.set_password(nuevaClave)
                user.save()

                logout(request)
                messages.success(request,'Contraseña cambiada con exito, por favor inicie sesión nuevamente')
                return redirect('mostrarLogin')
        
        else:
            messages.warning(request,'Algo salío mal')
            return redirect('mostrarCambioClave')
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')
    
def eliminarCuenta(request):
    if request.user.is_authenticated:

        if request.method == 'POST':

            correo = request.session.get('correo', None)
            clave = request.POST.get('clave', None)
            confirmacion = request.POST.get('confirmar', None)

            if not request.user.check_password(clave):
                messages.error(request,'La contraseña ingresada no es correcta!')
                return redirect('mostrarEliminarCuenta')

            
            if confirmacion.strip() != 'ELIMINAR':
                messages.error(request,'Debe escribir ELIMINAR para confirmar la eliminación de la cuenta!')
                return redirect('mostrarEliminarCuenta')

            try:
                with transaction.atomic():
                    usuario = get_object_or_404(Usuario, correo=correo)
                    user = request.user

                    Peticiones.objects.filter(usuario=usuario).delete()
                    user.delete()
                    usuario.delete()
                    
                    logout(request)
                    messages.error(request,"Cuenta eliminada con éxito")
                    return redirect('mostrarIndex')
                
            except Exception as e:
                messages.error(request,"Error al eliminar la cuenta:", str(e))
                return redirect('mostrarEliminarCuenta')
        else:
            messages.warning(request,'Algo salío mal')
            return redirect('mostrarEliminarCuenta')
    else:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')

def definirParametros(request):
    if request.user.is_authenticated == False:
        messages.warning(request,'Debes iniciar sesión  para acceder a este contenido!')
        return redirect('mostrarLogin')
    
    rol = request.session.get('rol', None)

    if rol != 0:
        messages.warning(request,'No tiene rol estudiante!')
        return redirect('mostrarIndex')
    
    if request.method == 'POST':

        correo = request.session.get('correo', None)
        usuario = Usuario.objects.get(correo=correo)
        parametros = Parametros.objects.get(idParametros=usuario)

        comuna = request.POST.get('comuna')
        comunaRelevancia = request.POST.get('toggleComuna')

        budget = request.POST.get('presupuesto', None)
        budgetRelevancia = request.POST.get('togglePresupuesto')

        gratuidad = request.POST.get('gratuidad')
        gratuidadRelevancia = request.POST.get('toggleGratuidad')

        acreditacion = request.POST.get('acreditacion')
        acreditacionRelevancia = request.POST.get('toggleAcreditacion')

        esUniversidad = request.POST.get('EsUni')
        esUniversidadRelevancia = request.POST.get('toggleUni')

        puntajeNem = request.POST.get('nem')
        puntajeNemRelevancia = request.POST.get('toggleNem')

        carrera = request.POST.get('carrera')
        carreraRelevancia = request.POST.get('toggleCarrera')



        
        parametros.comunaRelevancia = bool(comunaRelevancia)
        parametros.budgetRelevancia = bool(budgetRelevancia)
        parametros.gratuidadRelevancia = bool(gratuidadRelevancia)
        parametros.acreditacionRelevancia = bool(acreditacionRelevancia)
        parametros.esUniversidadRelevancia = bool(esUniversidadRelevancia)
        parametros.puntajeNemRelevancia = bool(puntajeNemRelevancia)
        parametros.carreraRelevancia = bool(carreraRelevancia)


        if comunaRelevancia and comuna:
            usuario.comunaUsuario = comuna
        
        if budgetRelevancia and budget:
            parametros.budget = int(budget)
        
        if gratuidadRelevancia and gratuidad:
            parametros.gratuidad = (gratuidad == 'si')

        if esUniversidadRelevancia and esUniversidad:
            parametros.esUniversidad = (esUniversidad == 'si')

        if acreditacionRelevancia and acreditacion:
            parametros.acreditacionDeseado = int(acreditacion)
    
        if puntajeNemRelevancia and puntajeNem:
            parametros.puntajeNem = int(puntajeNem)

        if carreraRelevancia and carrera:
            parametros.carrera = carrera
        
        usuario.save()
            
        parametros.save()
        messages.success(request,'Preferencias actualizadas con éxito')
        return redirect('mostrarRecomendaciones')
    else:
        messages.warning(request,'Algo salío mal')
        return redirect('mostrarFormularioEstudiante')
    
def calcular_score(usuario, idInsti):
    
    
    parametros = Parametros.objects.get(idParametros=usuario)
    insti = Institucion.objects.get(idInstitucion=idInsti)
    carreras = Carrera.objects.filter(institucion=insti)

    carrera = Carrera.objects.filter(institucion=insti, nombreCarrera=parametros.carrera).first()

    score = 0
    detalles = {}
    totalParam = 0

    if parametros.comunaRelevancia and usuario.comunaUsuario.strip() != "":
        totalParam +=1
        if usuario.comunaUsuario == insti.comunaInstitucion:
            score += 10
            detalles[f'La institución se ubica en '+insti.comunaInstitucion] = True
        else:
            detalles[f'La institución no se ubica en '+usuario.comunaUsuario] = False
    
    if parametros.gratuidadRelevancia:
        totalParam +=1
        if parametros.gratuidad == insti.adscritoGratuidad:
            score += 10
            detalles['Esta adscrita a la gratuidad'] = True
        else:
            detalles['No esta adscrita a la gratuidad'] = False
    
    if parametros.acreditacionRelevancia:
        totalParam +=1
        if insti.acreditacion >= parametros.acreditacionDeseado:
            score += 10
            detalles['Acreditación de '+ str(insti.acreditacion) + " años"] = True
        else:
            detalles['Acreditación de '+ str(insti.acreditacion) + " años"] = False
    
    if parametros.esUniversidadRelevancia:
        totalParam +=1
        if parametros.esUniversidad == insti.esUniversidadInsti:
            score += 10
            detalles['Es una universidad'] = True
        else:
            detalles['No es una universidad'] = False
    tieneCarrera = True

    if parametros.carreraRelevancia and parametros.carrera.strip() != "":
        totalParam +=1
        if carreras.filter(nombreCarrera=parametros.carrera).exists():
            score += 10
            detalles['Tiene la carrera '+parametros.carrera] = True
        else:
            tieneCarrera = False
            detalles['No tiene la carrera '+parametros.carrera] = False
    
    if tieneCarrera:
        if parametros.puntajeNemRelevancia: 
            totalParam +=1
            if carrera:


                if carrera.puntajeMinimo <= 300 and parametros.puntajeNem == 1:
                    score += 10
                    detalles['El puntaje NEM te alcanza'] = True
                elif carrera.puntajeMinimo > 300 and parametros.puntajeNem == 1:   
                    detalles['El puntaje no NEM te alcanza'] = False

                if (carrera.puntajeMinimo > 300 and carrera.puntajeMinimo <= 500 )and parametros.puntajeNem == 2:
                    score += 10
                    detalles['El puntaje NEM te alcanza'] = True
                elif carrera.puntajeMinimo > 500 and parametros.puntajeNem == 2:
                    detalles['El puntaje no NEM te alcanza'] = False

                if (carrera.puntajeMinimo > 500 and carrera.puntajeMinimo <= 700  )and parametros.puntajeNem == 3:
                    score += 10
                    detalles['El puntaje NEM te alcanza'] = True
                elif carrera.puntajeMinimo > 700 and parametros.puntajeNem == 3:
                    detalles['El puntaje no NEM te alcanza'] = False

                if (carrera.puntajeMinimo > 700 and carrera.puntajeMinimo <= 900  )and parametros.puntajeNem == 4:
                    score += 10
                    detalles['El puntaje NEM te alcanza'] = True
                elif carrera.puntajeMinimo > 900 and parametros.puntajeNem == 4:
                    detalles['El puntaje no NEM te alcanza'] = False

                if (carrera.puntajeMinimo > 900 and carrera.puntajeMinimo <= 1000 )and parametros.puntajeNem == 5:
                    score += 10
                    detalles['El puntaje NEM te alcanza'] = True
                
        
        if parametros.budgetRelevancia and parametros.budget != 0:
            totalParam +=1
            if carrera: 
                
                if parametros.gratuidad and insti.adscritoGratuidad:
                    score += 10
                    detalles['La gratuidad lo cubre'] = True 
                else:


                    if carrera.costo <= 3000000 and parametros.budget == 1:
                        score += 10
                        detalles['Tu presupuesto alcanza'] = True 
                    elif parametros.budget == 1 and carrera.costo > 3000000:
                        detalles['Tu presupuesto no alcanza'] = False
                    
                    if (carrera.costo > 3000000 and carrera.costo <= 5000000) and parametros.budget == 2:
                        score += 10
                        detalles['Tu presupuesto alcanza'] = True 
                    elif parametros.budget == 2 and carrera.costo > 5000000:
                        detalles['Tu presupuesto no alcanza'] = False

                    if (carrera.costo > 5000000 and carrera.costo <= 7000000) and parametros.budget == 3:
                        score += 10
                        detalles['Tu presupuesto alcanza'] = True 
                    elif parametros.budget == 3 and carrera.costo > 7000000:
                        detalles['Tu presupuesto no alcanza'] = False

                    if (carrera.costo > 7000000 and carrera.costo <= 10000000) and parametros.budget == 4:
                        score += 10
                        detalles['Tu presupuesto alcanza'] = True 
                    elif parametros.budget == 4 and carrera.costo > 10000000:
                        detalles['Tu presupuesto no alcanza'] = False

                    if carrera.costo >= 10000000 and parametros.budget == 5:
                        score += 10
                        detalles['Tu presupuesto alcanza'] = True
            
            

    totalParam *=10 

    if totalParam == 0:
        porcentaje = 100
    else:
        porcentaje = round((score / totalParam) * 100, 2)
    
    return score, porcentaje, detalles


    
def generar_recomendaciones(usuario, uni):
    
    if uni:
        instituciones = Institucion.objects.filter(tipoInstitucion = 'Universidad')
    else:
        instituciones = Institucion.objects.all()
    
    recomendaciones = []
    for insti in instituciones:
        score, porcentaje, detalles = calcular_score(usuario, insti.idInstitucion)
        recomendaciones.append({
            "institucion": insti,
            "score": score,
            "porcentaje": porcentaje,
            "detalles" : detalles
        })
    recomendaciones.sort(key=lambda x: (x["porcentaje"]), reverse=True)
    return recomendaciones


