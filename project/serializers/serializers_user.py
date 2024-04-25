from rest_framework import serializers
from ..models.models_user import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
