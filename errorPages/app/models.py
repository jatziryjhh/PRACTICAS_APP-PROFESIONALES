from django.db import models

# Create your models here.
#modelos son objetos o una entidad de la base de datos
#se pueden crear modelos o tablas en la base de datos

#copiamos y pegamos lo que salio en la consola al hacer python manage.py inspectdb
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Mascotas(models.Model):
    nombre = models.CharField(max_length=60, blank=True, null=True)
    
    
#en consola escribir python manage.py makemigrations

#vamos a usar python manage.py migrate --fake-initial para que no cree la tabla de nuevo de usuarios
class Usuarios(models.Model):
    nombres = models.CharField(max_length=60, blank=True, null=True)
    apellidos = models.CharField(max_length=60, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'

class ErrorLog(models.Model):
    codigo = models.CharField(max_length=10)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.codigo} - {self.mensaje}"