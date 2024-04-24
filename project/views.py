from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializers
from .serializers import ServiceSerializers
from .models import User
from .models import Service
from rest_framework import status
from django.http import Http404
from .pagination import MyCustomPagination

# Create your views here.

class UserView(APIView):
    "Class articulo to call apia and his methods"

    def get_object(self, pk):
        #TODO : revisar
        "Get only one user"
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        "Get many Users"
        json_response = {}
        role_default = "normal"
        role_param = role_default
        users = User.objects.all().filter(role=role_param)

        users_len = len(users)
        pagination_class = MyCustomPagination()
        result_page = pagination_class.paginate_queryset(users, request)
        serializer_users = UserSerializers(result_page, many=True)
        
        
        json_response['total_users'] = users_len
        json_response['message'] = 'Succesfully'
        json_response['data'] = serializer_users.data

        return Response(json_response, status=status.HTTP_200_OK)


    def post(self, request):
        #TODO falta cargar por excel
        "Insert one or many users"
        users_request = request.data
        json_response = {}
        if isinstance(users_request, list):
            serializer_user = UserSerializers(data=users_request, many=True)
        else:
            serializer_user = UserSerializers(data=users_request)

        if serializer_user.is_valid():
            serializer_user.save()
            json_response['message'] = 'Succesfully'
            json_response['data'] = serializer_user.data
            return Response(json_response, status=status.HTTP_201_CREATED)
        json_response['message'] = serializer_user.errors
        json_response['data'] = []
        return Response(json_response, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        "Update a user"
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
        user = self.get_object(pk)
        serializer = UserSerializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            json_response['message'] = 'Succesfully'
            json_response['data'] = serializer.data
            return Response(json_response, status=status.HTTP_200_OK)
        json_response['message'] = serializer.errors
        json_response['data'] = []
        return Response(json_response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        "Delete one or many users"
        json_response = {}
        if request.query_params.get('pks') is None :
            json_response['message'] = 'The pks parameter is required'
            json_response['data'] = None
            return Response(json_response, status=status.HTTP_400_BAD_REQUEST)
        pks = request.query_params.get('pks').split(',')
        if pks:
            user = User.objects.filter(id__in=pks)
            user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ServiceView(APIView):
    def get_object(self, pk):
        #TODO : revisar
        "Get only one user"
        try:
            return Service.objects.get(pk=pk)
        except service.DoesNotExist:
            raise Http404

    def get(self, request):
        "Get many services"
        json_response = {}
        role_default = "normal"
        role_param = role_default
        services = Service.objects.all().filter(role=role_param)

        services_len = len(services)
        pagination_class = MyCustomPagination()
        result_page = pagination_class.paginate_queryset(services, request)
        serializer_services = serviceSerializers(result_page, many=True)
        
        
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
