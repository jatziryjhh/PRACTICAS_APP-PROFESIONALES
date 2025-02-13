from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        
        #Que campos quiero que se muestren en el formulario
        fields = ['nombre','imagen']
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa aqui el nombre del categoria'}),
            'imagen': forms.URLInput(attrs={'class':'form-control','placeholder':'Ingresa aqui la URL de la imagen del categoria'}),
        }

    #etiquetas
    labels = {
        'nombre': 'Nombre de la categoria',
        'imagen': 'URL de la Imagen'
    }

    #personalizar los mensajes de error
    error_messages = {
        'nombre': {
            'required': 'El campo nombre es obligatorio',
            "invalid": "El nombre no es valido"
        },
        'imagen': {
            'required': 'El campo Imagen es obligatorio'
        }
    }
