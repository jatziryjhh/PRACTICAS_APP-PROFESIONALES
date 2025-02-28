from django import forms
from .models import Alumnos

class AlumnosForm(forms.ModelForm):
    class Meta:
        model=Alumnos
        
        #Que campos quiero que se muestren en el formulario
        fields = ['nombre','apellido','edad','matricula','correo']
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa aqui el nombre del Alumnos'}),
            'apellido': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa aqui el apellido del Alumnos'}),
            'edad': forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingresa aqui la edad del Alumnos'}),
            'matricula': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa aqui la matricula del Alumnos'}),
            'correo': forms.EmailInput(attrs={'class':'form-control','placeholder':'Ingresa aqui el correo del Alumnos'}),
        }

    #etiquetas
    labels = {
        'nombre': 'Nombre del Alumnos',
        'apellido': 'Apellido del Alumnos',
        'edad': 'Edad del Alumnos',
        'matricula': 'Matricula del Alumnos',
        'correo': 'Correo del Alumnos'
    }

    #personalizar los mensajes de error
    error_messages = {
        'nombre': {
            'required': 'El campo nombre es obligatorio',
            "invalid": "El nombre no es valido"
        },
        'apellido': {
            'required': 'El campo apellido es obligatorio'
        },
        'edad': {
            'required': 'El campo edad es obligatorio'
        },
        'matricula': {
            'required': 'El campo matricula es obligatorio'
        },
        'correo': {
            'required': 'El campo correo es obligatorio'
        }
    }