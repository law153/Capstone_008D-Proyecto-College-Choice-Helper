from django.shortcuts import render, redirect
from .models import Usuario, Rol, Parametros
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.db import transaction

# Sin cuenta
def mostrarIndex(request):
    return render(request, 'core/index.html')

def mostrarLogin(request):
    return render(request, 'core/sinCuenta/login.html')

def mostrarRegistro(request):
    return render(request, 'core/sinCuenta/registrarse.html')

def mostrarOlvidoClave(request):
    return render(request, 'core/sinCuenta/olvideClave.html')

def inicioSesion(request):
    if request.method == 'POST':
        correoI = request.POST.get('correo_ini')
        contrasenaI = request.POST.get('contrasena_ini')

        userAuth = authenticate(username = correoI, password = contrasenaI)

        print(correoI, contrasenaI)

        if userAuth is not None:

            login(request, userAuth)

            usuario = Usuario.objects.get(correo = correoI)

            print("Eu rol es: ", usuario.rol.nombre_rol)
            
            request.session['rol'] = usuario.rol.id_rol
            request.session['correo'] = userAuth.username

            return redirect('mostrarIndex')
        else:
            print("El correo o la contraseña son incorrectos")
            return redirect('mostrarLogin')
    else:
        return redirect('mostrarLogin')
    
def registrarUsuario(request):
    if request.method == 'POST':

        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        contrasena_rep = request.POST.get('contrasena_rep')

        if User.objects.filter(username=correo).exists():
            print("El correo ya está registrado")
            return redirect('mostrarRegistro')
        
        if contrasena != contrasena_rep:
            print("Las contraseñas no coinciden")
            return redirect('mostrarRegistro')
        
        try:

            with transaction.atomic():

                user = User.objects.create_user(username=correo, password=contrasena, email=correo)
                user.is_staff = False
                user.is_active = True
                user.save()

                registroRol = Rol.objects.get(id_rol = 1)
                usuario = Usuario.objects.create(idUsuario = user, correo = correo, rol = registroRol)
                    
                Parametros.objects.create(idParametros = usuario)

            print("Usuario registrado exitosamente")
            return redirect('mostrarIndex')
        
        except Exception as e:
            print("Error al registrar el usuario:", e)
            return redirect('mostrarRegistro')
            
        
    else:
        return redirect('mostrarRegistro')