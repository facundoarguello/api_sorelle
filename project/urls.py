from django.urls import path
from .views.view_user import UserView
from .views.view_service import ServiceView

urlpatterns =[
    path('users/', UserView.as_view(), name='user_list'),
    path('services/', ServiceView.as_view(), name='services_list'),
    
]