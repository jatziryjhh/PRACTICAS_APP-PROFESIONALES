from django.db import models
from django.forms import ValidationError

#clase de productos
class Alumnos(models.Model):
    #atributos de la clase
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    matricula = models.CharField(max_length=50, unique=True)
    correo = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nombre

    
    #Necesito una funcion que devuelva el objeto en forma de Dict
    def to_dict(self):
        return {
            #claveValor:"valor"
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'matricula': self.matricula,
            'correo': self.correo
        }