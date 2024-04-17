from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializers
from .models import User
from rest_framework import status
from django.http import Http404
from .pagination import MyCustomPagination

# Create your views here.

class UserView(APIView):
    "Class articulo to call apia and his methods"

    def get_object(self, pk):
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
