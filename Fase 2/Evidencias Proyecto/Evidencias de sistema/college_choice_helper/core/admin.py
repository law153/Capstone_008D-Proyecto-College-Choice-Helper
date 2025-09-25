from django.contrib import admin
from .models import Rol, Usuario, Parametros, Institucion, Carrera, Peticiones
# Register your models here.

admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Parametros)
admin.site.register(Institucion)
admin.site.register(Carrera)
admin.site.register(Peticiones)