from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.URLField()
    def __str__(self):
        return self.nombre
    
    def to_categoria(self):
        return {
            'nombre': self.nombre,
            'imagen': self.imagen
        }