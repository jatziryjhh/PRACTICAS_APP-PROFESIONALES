from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from .models import CustomUser
import re

#primer formulario (registro)
class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'pattern': '^(?=.*\d)(?=.*[!#$%&?]).{8,}$',
                'placeholder': 'Ingresa tu contraseña',
                'title': 'Necesitas definir una contraseña segura, al menos 8 caracteres, un numero y un caracter especial',
                'required': True
            }
        )
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'pattern': '^(?=.*\d)(?=.*[!#$%&?]).{8,}$',
                'placeholder': 'Repite tu contraseña',
                'title': 'Las contraseñas deben coincidir',
                'required': True
            }
        )
    )
    
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel','password1', 'password2']
        #si quiero editar la forma de los inputs necesito widgets
        widgets = {
            #cada uno de los widgets es un input
            #cada uno de los widgets del **MODELO**
            'email': forms.EmailInput(
                #caracterisitcas del elemento visual
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': '^[a-zA-Z0-9]+@utez\.edu\.mx$',
                    'title': 'Debes ingresar un correo electronico valido de la UTEZ'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': '^[a-zA-Z ]+$',
                    'title': 'Solo se permiten letras',
                    'placeholder': 'Ingresa tu nombre'
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': '^[a-zA-Z ]+$',
                    'title': 'Solo se permiten letras',
                    'placeholder': 'Ingresa tu apellido'
                }
            ),
            'control_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': '^(I)?\d{5}[a-zA-Z]{2}\d{3}$',
                    'title': 'Tu formato es valido con ingenieria o sin ella, pero de la UTEZ',
                    'placeholder': 'Ingresa tu numero de control'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': '^[0-9]{2,}$',
                    'title': 'Solo se permiten numeros',
                    'placeholder': 'Ingresa tu edad'
                }
            ),
            'tel': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': '^\d{10}$',
                    'title': 'Debe ser un número de 10 dígitos',
                    'placeholder': 'Ingresa tu teléfono',
                    'minlength': '10',
                    'maxlength': '10'}
            )
        }


#Segundo formulario (inicio de sesion)
class CustomUserLoginForm(AuthenticationForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'required': True,
        'placeholder': 'Ingresa tu contraseña',
        'title': 'Contraseña de al menos 8 caracteres, con un símbolo y un número'
    }))

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8 or not re.search(r'[!#$%&?]', password) or not re.search(r'\d', password):
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres, un número y un símbolo (!, #, $, %, & o ?).")
        return password

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            # Busca al usuario por email (suponiendo que en tu modelo el email es el campo username)
            user = authenticate(request=self.request, username=email, password=password)
            if user is None:
                raise ValidationError("Correo o contraseña incorrectos.")
        
        return cleaned_data