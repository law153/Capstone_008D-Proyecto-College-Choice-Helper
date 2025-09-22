from django.shortcuts import render

#Admin
def mostrarGestionEstu(request):
    return render (request,'core/admin/gestionEstudiantes.html')

def mostrarGestionInsti(request):
    return render (request,'core/admin/gestionInstituciones.html')

