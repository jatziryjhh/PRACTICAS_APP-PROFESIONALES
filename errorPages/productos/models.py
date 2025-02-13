from django.db import models

#clase de productos
class Producto(models.Model):
    #atributos de la clase
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    Imagen = models.URLField()

    def __str__(self):
        return self.nombre
    
    #Necesito una funcion que devuelva el objeto en forma de Dict
    def to_dict(self):
        return {
            #claveValor:"valor"
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'imagen': self.Imagen
        }