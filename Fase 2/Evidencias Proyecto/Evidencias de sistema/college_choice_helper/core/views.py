from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout

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