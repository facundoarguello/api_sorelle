from django.urls import path
from .views.view_user import UserView
from .views.view_service import ServiceView
from .views.view_reservation import ReservationView

urlpatterns =[
    path('users/', UserView.as_view(), name='user_list'),
    path('services/', ServiceView.as_view(), name='services_list'),
    path('reservation/', ReservationView.as_view(), name='reservation_list'),
    
]