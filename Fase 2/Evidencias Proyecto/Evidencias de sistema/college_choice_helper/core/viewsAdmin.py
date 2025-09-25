from django.shortcuts import render

#Admin
def mostrarGestionEstu(request):
    return render (request,'core/admin/gestionEstudiantes.html')

def mostrarGestionInsti(request):
    return render (request,'core/admin/gestionInstituciones.html')

def mostrarVerPeticiones(request):
    return render (request,'core/admin/verPeticiones.html')

def mostrarVerPeticion(request):
    return render (request,'core/admin/verPeticion.html')

