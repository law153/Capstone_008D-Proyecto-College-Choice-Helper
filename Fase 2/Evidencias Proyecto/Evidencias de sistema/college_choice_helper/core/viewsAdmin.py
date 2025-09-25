from django.shortcuts import render

#Admin
def mostrarGestionEstu(request):
    rol = request.session.get('rol', None)

    contexto = {'rol': rol}
    return render (request,'core/admin/gestionEstudiantes.html', contexto)

def mostrarGestionInsti(request):
    rol = request.session.get('rol', None)

    contexto = {'rol': rol}
    return render (request,'core/admin/gestionInstituciones.html', contexto)

def mostrarVerPeticiones(request):
    rol = request.session.get('rol', None)

    contexto = {'rol': rol}
    return render (request,'core/admin/verPeticiones.html', contexto)

def mostrarVerPeticion(request):
    rol = request.session.get('rol', None)

    contexto = {'rol': rol}

    return render (request,'core/admin/verPeticion.html', contexto)

