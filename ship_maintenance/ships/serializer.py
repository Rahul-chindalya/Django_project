from rest_framework.serializers import serializer
from .models import Ship

class ShipSerializer(serializer.ModelSerializer):
    class Meta:
        model = Ship
        fields = '__all__'
        