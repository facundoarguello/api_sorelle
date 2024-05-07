from rest_framework import serializers
from ..models.models_reservation import Reservation
from datetime import datetime



class ReservationSerializers(serializers.ModelSerializer):
    def create(self, validated_data):
        date_reservation = validated_data['date']
        professional = validated_data['professional']
        client = validated_data['client']
        current_date = datetime.date(datetime.now())
        
        if date_reservation < current_date:
            raise serializers.ValidationError("The date is lower than the current date")
        if client == professional:
            raise serializers.ValidationError("The client and profesional has same id")

        return super().create(validated_data)
    class Meta:
        model = Reservation
        fields = '__all__'