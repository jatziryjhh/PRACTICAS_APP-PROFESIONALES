from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        
        #Que campos quiero que se muestren en el formulario
        fields = ['nombre','precio','Imagen']
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa aqui el nombre del producto'}),
            'precio': forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingresa aqui el precio del producto'}),
            'Imagen': forms.URLInput(attrs={'class':'form-control','placeholder':'Ingresa aqui la URL de la imagen del producto'}),
        }

    #etiquetas
    labels = {
        'nombre': 'Nombre del Producto',
        'precio': 'Precio del Producto',
        'Imagen': 'URL de la Imagen'
    }

    #personalizar los mensajes de error
    error_messages = {
        'nombre': {
            'required': 'El campo nombre es obligatorio',
            "invalid": "El nombre no es valido"
        },
        'precio': {
            'required': 'El campo precio es obligatorio'
        },
        'Imagen': {
            'required': 'El campo Imagen es obligatorio'
        }
    }

    