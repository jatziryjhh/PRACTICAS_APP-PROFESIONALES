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
                    'pattern': '^[a-zA-ZÀ-ÿ\s]+$',
                    'title': 'Solo se permiten letras',
                    'placeholder': 'Ingresa tu nombre'
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': '^[a-zA-ZÀ-ÿ\s]+$',
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
                    'placeholder': 'Ingresa tu numero de control',
                    'maxlength':20
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': '^[0-9]{2,}$',
                    'title': 'Solo se permiten numeros',
                    'placeholder': 'Ingresa tu edad',
                    'minlength':1,
                    'maxlength':100
                }
            ),
            'tel': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'pattern': '^[0-9]{10}$',
                    'title': 'Debe ser un número de 10 dígitos',
                    'placeholder': 'Ingresa tu teléfono',
                    'maxlength': '10'
                }
            )
        }
        
        def clean_email(self):
            email = self.cleaned_data.get("email")
            if not re.match(r'^[a-zA-Z0-9]+@utez\.edu\.mx$', email):
                raise forms.ValidationError("El correo electrónico debe ser de la UTEZ.")
            return email
        
        def clean_control_number(self):
            control_number = self.cleaned_data.get("control_number")
            if not re.match(r'^(I)?\d{5}[a-zA-Z]{2}\d{3}$', control_number):
                raise forms.ValidationError("El número de control debe tener el formato correcto.")
            return control_number
            
        def clean_tel(self):
            tel = self.cleaned_data.get("tel")
            # Validación de que el teléfono tiene exactamente 10 dígitos
            if len(str(tel)) != 10:
                raise forms.ValidationError("El teléfono debe tener exactamente 10 dígitos.")
            return tel
        
        def clean_password1(self):
            password1 = self.cleaned_data.get("password1")
            if len(password1) < 8:
                raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
            if not re.search(r'\d', password1):
                raise forms.ValidationError("La contraseña debe contener al menos un número.")
            if not re.search(r'[A-Z]', password1):
                raise forms.ValidationError("La contraseña debe contener al menos una letra mayúscula.")
            if not re.search(r'[!#$%&?]', password1):
                raise forms.ValidationError("La contraseña debe contener al menos un símbolo (!, #, $, %, & o ?).")
            return password1
        
        def clean_password2(self):
            password2 = self.cleaned_data.get("password2")
            password1 = self.cleaned_data.get("password1")
            # Validación de que las contraseñas coincidan
            if password1 != password2:
                raise forms.ValidationError("Las contraseñas no coinciden.")
            return password2

        def clean_age(self):
            age = self.cleaned_data.get("age")
            if age < 18:
                raise forms.ValidationError("Debes ser mayor de edad para registrarte.")
            return age
    
        def clean(self):
            cleaned_data = super().clean()
            return cleaned_data


#Segundo formulario (inicio de sesion)
class CustomUserLoginForm(AuthenticationForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'required': True,
        'placeholder': 'Ingresa tu contraseña',
        'title': 'Contraseña de al menos 8 caracteres, con un símbolo y un número'
    }))
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not re.match(r'^[a-zA-Z0-9]+@utez\.edu\.mx$', email):
            raise forms.ValidationError("El correo electrónico debe ser de la UTEZ.")
        return email

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
            user = authenticate(request=self.request, username=email, password=password)
            if user is None:
                raise ValidationError("Correo o contraseña incorrectos.")
        
        return cleaned_data