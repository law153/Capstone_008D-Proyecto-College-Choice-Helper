from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate
from .models import Usuario, Rol, Peticiones, Institucion, Parametros, Carrera
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import transaction
from django.contrib.auth.hashers import check_password

# Estudiantes
def mostrarFormularioEstudiante(request):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)

        contexto = {'rol': rol}
        return render(request, 'core/estudiantes/formularioEstudiante.html', contexto)
    else:
        print("Debe iniciar sesión para acceder a este contenido")
        return redirect('mostrarLogin')

def mostrarRecomendaciones(request):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)

        contexto = {'rol': rol}
        return render(request, 'core/estudiantes/recomendaciones.html', contexto)
    else:
        print("Debe iniciar sesión para acceder a este contenido")
        return redirect('mostrarLogin')

def mostrarVistaInstituciones(request):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)

        contexto = {'rol': rol}
        return render(request, 'core/estudiantes/vistaInstitucion.html', contexto)
    else:
        print("Debe iniciar sesión para acceder a este contenido")
        return redirect('mostrarLogin')
    

def mostrarCambioClave(request):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)


        contexto = {'rol': rol}
        return render(request, 'core/estudiantes/cambiarClave.html', contexto)
    else:
        print("Debe iniciar sesión para acceder a este contenido")
        return redirect('mostrarLogin')

def mostrarCambioCorreo(request):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)

        contexto = {'rol': rol}
        return render(request, 'core/estudiantes/cambiarCorreo.html', contexto)
    else:
        print("Debe iniciar sesión para acceder a este contenido")
        return redirect('mostrarLogin')

def mostrarGestionCuenta(request):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)

        contexto = {'rol': rol}
        return render(request, 'core/estudiantes/gestionCuenta.html', contexto)
    else:
        print("Debe iniciar sesión para acceder a este contenido")
        return redirect('mostrarLogin')

def mostrarHacerPeticion(request):
    if request.user.is_authenticated:
        rol = request.session.get('rol', None)

        contexto = {'rol': rol}
        return render(request, 'core/estudiantes/hacerPeticion.html', contexto)
    else:
        print("Debe iniciar sesión para acceder a este contenido")
        return redirect('mostrarLogin')

def cierreSesion(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('mostrarIndex')
    else:
        print("Debe iniciar sesión para acceder a este contenido")
        return redirect('mostrarLogin')

def generarPeticion(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            correo = request.session.get('correo', None)
            usuario = Usuario.objects.get(correo=correo)

            asunto = request.POST.get('asunto')
            tipoPeticion = request.POST.get('tipo')
            mensaje = request.POST.get('mensaje')

            Peticiones.objects.create(asunto = asunto, tipoPeticion = tipoPeticion, mensaje = mensaje, usuario = usuario)
            print("Petición creada con éxito")
            return redirect('mostrarHacerpeticion')

        else:
            print("Petición fallada :,c", asunto, tipoPeticion, mensaje, correo)
            return redirect('mostrarHacerpeticion')
    else:
        print("Debe iniciar sesión para acceder a este contenido")
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
                print("Los contraseña es incorrecta")
                return redirect('mostrarCambioCorreo')
            
            if User.objects.filter(username=nuevoCorreo).exists():
                print("Ese correo ya está en uso.")
                return redirect('mostrarCambioCorreo')
            
            try:
                validate_email(nuevoCorreo)
            except ValidationError:
                print("El correo no es válido")
                return redirect('mostrarCambioCorreo')

            if nuevoCorreo != repetirCorreo:
                print("Los correos no coinciden")
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
                print("Correo cambiado con éxito, por favor inicie sesión nuevamente")
                return redirect('mostrarLogin')
        
        else:
            print("Error en la solicitud")
            return redirect('mostrarCambioCorreo')
    else:
        print("Debe iniciar sesión para acceder a este contenido")
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
                print("Los contraseña es incorrecta")
                return redirect('mostrarCambioClave')
            
            if check_password(nuevaClave, request.user.password):
                print("La nueva contraseña no puede ser igual a la actual")
                return redirect('mostrarCambioClave')

            if nuevaClave != repetirClave:
                print("Las claves no coinciden")
                return redirect('mostrarCambioClave')

            try:
                validate_password(nuevaClave, user=request.user)
            except ValidationError as e:
                for error in e:
                    print(error)
                return redirect('mostrarCambioClave')

            
            
            with transaction.atomic():
                user = request.user
                user.set_password(nuevaClave)
                user.save()

                logout(request)
                print("Contraseña cambiado con éxito, por favor inicie sesión nuevamente")
                return redirect('mostrarLogin')
        
        else:
            print("Error en la solicitud")
            return redirect('mostrarCambioClave')
    else:
        print("Debe iniciar sesión para acceder a este contenido")
        return redirect('mostrarLogin')
    



