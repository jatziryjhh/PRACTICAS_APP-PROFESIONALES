from rest_framework import serializers
from .models import Alumnos

#clase que serializa los productos
class AlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = '__all__'