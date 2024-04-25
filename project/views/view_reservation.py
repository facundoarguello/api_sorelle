from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models.functions import ExtractMonth
from django.http import Http404
from ..serializers.serializers_reservation import ReservationSerializers
from ..models.models_reservation import Reservation

class ReservationView(APIView):
    def get_object(self, pk):
        #TODO : revisar
        "Get only one user"
        try:
            return Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            raise Http404

    def get(self, request):
        "Get many reservation"
        json_response = {}
        date_param = self.request.query_params.get('date', None)
        month = self.request.query_params.get('month', None)
        service = self.request.query_params.get('service', None)
        profesional = self.request.query_params.get('profesional', None)
        if service :
            if not isinstance(service,int):
                json_response['message'] = 'The service parameter will be a number'
                json_response['data'] = None
                return Response(json_response, status=status.HTTP_400_BAD_REQUEST)
        if month :
            if not isinstance(month,int):
                json_response['message'] = 'The month parameter will be a number'
                json_response['data'] = None
                return Response(json_response, status=status.HTTP_400_BAD_REQUEST)


        reservation = Reservation.objects.select_related().all()

        if date_param:
            reservation = reservation.filter(date__gte=date_param,date__lte=date_param)
        if month:
            reservation = reservation.filter(date__month=month)
        if service:
            reservation = reservation.filter(service=service)
        if profesional:
            reservation = reservation.filter(professional=profesional)
        services_len = len(reservation)

        reservation_serializer = ReservationSerializers(reservation, many=True)
        
        
        json_response['total_reservation'] = services_len
        json_response['message'] = 'Succesfully'
        json_response['data'] = reservation_serializer.data

        return Response(json_response, status=status.HTTP_200_OK)


    def post(self, request):
        #TODO falta cargar por excel
        "Insert one or many reservation"
        services_request = request.data
        json_response = {}
        if isinstance(services_request, list):
            serializer_service = ReservationSerializers(data=services_request, many=True)
        else:
            serializer_service = ReservationSerializers(data=services_request)

        if serializer_service.is_valid():
            serializer_service.save()
            json_response['message'] = 'Succesfully'
            json_response['data'] = serializer_service.data
            return Response(json_response, status=status.HTTP_201_CREATED)
        json_response['message'] = serializer_service.errors
        json_response['data'] = []
        return Response(json_response, status=status.HTTP_400_BAD_REQUEST)


