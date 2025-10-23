from django.shortcuts import render, redirect
from .models import Usuario, Rol, Parametros, Peticiones
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.db import transaction
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib import messages

# Sin cuenta
def mostrarIndex(request):
    rol = request.session.get('rol', None)

    contexto = {'rol': rol}


    return render(request, 'core/index.html', contexto)

def mostrarLogin(request):
    if request.user.is_authenticated == False:
        return render(request, 'core/sinCuenta/login.html')
    else:
        messages.warning(request,'Ya has iniciado sesión!')
        return redirect('mostrarIndex')
    
def mostrarRegistro(request):
    if request.user.is_authenticated == False: 
        return render(request, 'core/sinCuenta/registrarse.html')
    else:
        messages.warning(request,'Ya has iniciado sesión!')
        return redirect('mostrarIndex')

def mostrarOlvidoClave(request):
    if request.user.is_authenticated == False:
        return render(request, 'core/sinCuenta/olvideClave.html')
    else:
        messages.warning(request,'Ya has iniciado sesión!')
        return redirect('mostrarIndex')

def inicioSesion(request):
    if request.user.is_authenticated:
        messages.warning(request,'Ya has iniciado sesión!')
        return redirect('mostrarIndex')
    
    if request.method == 'POST':
        correoI = request.POST.get('correo_ini')
        contrasenaI = request.POST.get('contrasena_ini')

        userAuth = authenticate(username = correoI, password = contrasenaI)


        if userAuth is not None:

            login(request, userAuth)

            usuario = Usuario.objects.get(correo = correoI)

            
            
            request.session['rol'] = usuario.rol.id_rol
            request.session['correo'] = usuario.correo

            return redirect('mostrarIndex')
        else:
            messages.error(request,'El correo o contraseña ingresados son incorrectos!')
            return redirect('mostrarLogin')
    else:
        return redirect('mostrarLogin')
    
def registrarUsuario(request):
    if request.user.is_authenticated:
        messages.warning(request, 'Ya has iniciado sesión!')
        return redirect('mostrarIndex')
    
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        contrasena_rep = request.POST.get('contrasena_rep')
        toggleRol = request.POST.get('toggleRol', None)

        
        try:
            validate_email(correo)
        except ValidationError:
            messages.error(request, 'El correo no es válido!')
            return redirect('mostrarRegistro')

        
        if contrasena != contrasena_rep:
            messages.error(request, 'Las contraseñas no coinciden!')
            return redirect('mostrarRegistro')

        
        usuario_existente = Usuario.all_objects.filter(correo=correo).first()

        
        if usuario_existente and usuario_existente.activo:
            messages.error(request, 'El correo ingresado ya está registrado!')
            return redirect('mostrarRegistro')

        
        if usuario_existente and not usuario_existente.activo:
            usuario_existente.restore()
            usuario_existente.idUsuario.is_active = True
            usuario_existente.idUsuario.save()
            messages.success(request, 'Tu cuenta ha sido restaurada correctamente.')
            return redirect('mostrarLogin')

        
        try:
            with transaction.atomic():
                user = User.objects.create_user(username=correo, password=contrasena, email=correo)
                user.is_staff = False
                user.is_active = True
                user.save()

                rol_estudiante = Rol.objects.get(id_rol=0)
                usuario = Usuario.objects.create(idUsuario=user, correo=correo, rol=rol_estudiante)
                Parametros.objects.create(idParametros=usuario)

                if toggleRol == 'on':
                    Peticiones.objects.create(
                        asunto="Solicitud de cuenta de Gestor de instituciones",
                        tipoPeticion="Cambio de rol",
                        mensaje=f"El usuario con correo {correo} solicita una cuenta de Gestor de instituciones.",
                        estadoPeticion="Pendiente",
                        usuario=usuario
                    )

            messages.success(request, 'Su cuenta se creó exitosamente!')
            return redirect('mostrarLogin')

        except Exception as e:
            messages.error(request, f"Error al registrar el usuario: {e}")
            return redirect('mostrarRegistro')

    return redirect('mostrarRegistro')
