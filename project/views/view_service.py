from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from ..serializers.serializers_service import ServiceSerializers
from ..models.models_service import Service
from ..pagination import MyCustomPagination

class ServiceView(APIView):
    def get_object(self, pk):
        #TODO : revisar
        "Get only one user"
        try:
            return Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            raise Http404

    def get(self, request):
        "Get many services"
        json_response = {}
        services = Service.objects.all().filter()

        services_len = len(services)
        pagination_class = MyCustomPagination()
        result_page = pagination_class.paginate_queryset(services, request)
        serializer_services = ServiceSerializers(result_page, many=True)
        
        
        json_response['total_services'] = services_len
        json_response['message'] = 'Succesfully'
        json_response['data'] = serializer_services.data

        return Response(json_response, status=status.HTTP_200_OK)


    def post(self, request):
        #TODO falta cargar por excel
        "Insert one or many services"
        services_request = request.data
        json_response = {}
        if isinstance(services_request, list):
            serializer_service = ServiceSerializers(data=services_request, many=True)
        else:
            serializer_service = ServiceSerializers(data=services_request)

        if serializer_service.is_valid():
            serializer_service.save()
            json_response['message'] = 'Succesfully'
            json_response['data'] = serializer_service.data
            return Response(json_response, status=status.HTTP_201_CREATED)
        json_response['message'] = serializer_service.errors
        json_response['data'] = []
        return Response(json_response, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        "Update a service"
        json_response = {}
        if request.query_params.get('pk') is None :
            json_response['message'] = 'The pk parameter is required'
            json_response['data'] = None
            return Response(json_response, status=status.HTTP_400_BAD_REQUEST)
        if request.body == {} :
            json_response['message'] = 'The body is required but is empty'
            json_response['data'] = None
            return Response(json_response, status=status.HTTP_400_BAD_REQUEST)
        
        pk = request.query_params.get('pk')
        service = self.get_object(pk)
        serializer = ServiceSerializers(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            json_response['message'] = 'Succesfully'
            json_response['data'] = serializer.data
            return Response(json_response, status=status.HTTP_200_OK)
        json_response['message'] = serializer.errors
        json_response['data'] = []
        return Response(json_response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        "Delete one or many services"
        json_response = {}
        if request.query_params.get('pks') is None :
            json_response['message'] = 'The pks parameter is required'
            json_response['data'] = None
            return Response(json_response, status=status.HTTP_400_BAD_REQUEST)
        pks = request.query_params.get('pks').split(',')
        if pks:
            service = Service.objects.filter(id__in=pks)
            service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
