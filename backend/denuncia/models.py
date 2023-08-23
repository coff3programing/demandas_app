from django.db import models

# Create your models here.
class Denuncia(models.Model):
    centro = models.BooleanField(default=False)
    delicia = models.BooleanField(default=False)
    calderon = models.BooleanField(default=False)
    quitumbe = models.BooleanField(default=False)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.BooleanField(default=False)
    pasaporte = models.BooleanField(default= False)
    numero_documento = models.CharField(max_length=100)
    calle_principal = models.CharField(max_length=100)
    numero_casa = models.CharField(max_length=100)
    calle_transversal = models.CharField(max_length=100)
    direccion_referencia = models.CharField(max_length=100)
    parroquia = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)
    numero_telefonico = models.CharField(max_length=10)
    numero_celular = models.CharField(max_length=10)
    email = models.EmailField()
    numero_casilla_judicial = models.CharField(max_length=10)
    parentesco_nna = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombres