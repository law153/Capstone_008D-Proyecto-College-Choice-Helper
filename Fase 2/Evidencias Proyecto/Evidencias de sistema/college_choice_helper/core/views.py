from django.shortcuts import render

# Sin cuenta
def mostrarIndex(request):
    return render(request, 'core/index.html')

def mostrarLogin(request):
    return render(request, 'core/sinCuenta/login.html')

def mostrarRegistro(request):
    return render(request, 'core/sinCuenta/registrarse.html')

def mostrarOlvidoClave(request):
    return render(request, 'core/sinCuenta/olvideClave.html')