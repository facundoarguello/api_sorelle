from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from ..models.models_user import User


class UserSerializers(serializers.ModelSerializer):
    firstname = serializers.CharField(max_length=255)
    lastname = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=500)
    birthdate = serializers.DateField()
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.password = validated_data.get('password', instance.password)
        return instance
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email' ,'birthdate' ,'role', 'datecreate', 'status', 'password', 'id']
