from django.db import models
from django.conf import settings
from django.utils import timezone

##Probando SoftDelete 
class SoftDeleteModel(models.Model):
    activo = models.BooleanField(default=True)
    fecha_eliminado = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.activo = False
        self.fecha_eliminado = timezone.now()
        self.save()

    def restore(self):
        self.activo = True
        self.fecha_eliminado = None
        self.save()

class ActivoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(activo=True)


# Create your models here.
class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True, verbose_name='0 para estudiante y 1 para institución, quiza 2 para admin')
    nombre_rol = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.nombre_rol
    
class Usuario(SoftDeleteModel):
    idUsuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    correo = models.CharField(max_length=50)
    comunaUsuario = models.CharField(max_length=50, default="")
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    objects = ActivoManager()
    all_objects = models.Manager() 

    def delete(self, *args, **kwargs):
        super(Usuario, self).delete(*args, **kwargs)
        if self.idUsuario:
            self.idUsuario.is_active = False
            self.idUsuario.save()

    def __str__(self):
        return self.correo

class Parametros(models.Model):
    idParametros = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    comunaRelevancia = models.BooleanField(default=True)
    budget = models.IntegerField(default=0)
    budgetRelevancia = models.BooleanField(default=True)
    gratuidad = models.BooleanField(default=False)
    gratuidadRelevancia = models.BooleanField(default=True)
    acreditacionDeseado = models.IntegerField(default=0)
    acreditacionRelevancia = models.BooleanField(default=True)
    tipoBuscado = models.CharField(max_length=50, default="")
    esUniversidadRelevancia = models.BooleanField(default=True)
    puntajeNem = models.IntegerField(default=100)
    puntajeNemRelevancia = models.BooleanField(default=True)
    carrera = models.CharField(max_length=100, default="")
    carreraRelevancia = models.BooleanField(default=True)



class Institucion(SoftDeleteModel):
    idInstitucion = models.AutoField(primary_key=True)
    nombreInstitucion = models.CharField(max_length=100)
    comunaInstitucion = models.CharField(max_length=50)
    fotoInstitucion = models.ImageField(default='default_insti.png')
    webInstitucion = models.CharField(max_length=100, default="") 
    adscritoGratuidad = models.BooleanField(default=False)
    acreditacion = models.IntegerField()
    tipoInstitucion = models.CharField(max_length=50, default="")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    objects = ActivoManager()
    all_objects = models.Manager() 
    def __str__(self) -> str:
        return self.nombreInstitucion
    
class Carrera(SoftDeleteModel):
    idCarrera = models.AutoField(primary_key=True)
    nombreCarrera = models.CharField(max_length=100)
    puntajeMinimo = models.IntegerField()
    costo = models.IntegerField(default=0)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    objects = ActivoManager()
    all_objects = models.Manager() 
    def __str__(self) -> str:
        return self.nombreCarrera

class Peticiones(models.Model):
    idPeticiones = models.AutoField(primary_key=True)
    asunto = models.CharField(max_length=100)
    tipoPeticion = models.CharField(max_length=50)
    mensaje = models.TextField()
    fechaPeticion = models.DateTimeField(auto_now_add=True)
    estadoPeticion = models.TextField(max_length=50, default="")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
