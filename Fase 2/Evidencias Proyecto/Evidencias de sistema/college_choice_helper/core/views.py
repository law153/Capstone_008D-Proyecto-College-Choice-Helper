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
    correoI = request.POST.get('correo_ini')
    contrasenaI = request.POST.get('contrasena_ini')

    print(correoI, contrasenaI)
    try:
        user = User.objects.get(username=correoI)
    except User.DoesNotExist:
        print("El usuario o la contraseña son incorrectos")
        return redirect('mostrarLogin')
    
    clave_valida = check_password(contrasenaI, user.password)

    if not clave_valida:
        print("Esa clave no es valida")
        return redirect('mostrarLogin')

    usuario = Usuario.objects.get(correo = correoI)

    userAuth = authenticate(username = correoI, password = contrasenaI)

    if userAuth is not None:
        login(request, userAuth)
        print("Eu rol es: ", usuario.rol.nombre_rol)
        return redirect('mostrarIndex')
    else:
        print("El usuario no existe")
        return redirect('mostrarLogin')