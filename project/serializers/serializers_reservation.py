from rest_framework import serializers
from ..models.models_reservation import Reservation


class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'