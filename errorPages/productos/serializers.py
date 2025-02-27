from rest_framework import serializers
from .models import Producto

#clase que serializa los productos
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'