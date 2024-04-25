from rest_framework import serializers
from ..models.models_service import Service


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'