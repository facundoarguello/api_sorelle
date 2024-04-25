from django.test import TestCase
import random
import json
# Create your tests here.

from ...models.models_service import Service
from django.urls import reverse

class ServiceViewTest(TestCase):

    def setUp(self):
        print("TESTING IN SERVICE")
        print("creation 15 services")
        number_of_users = 15
        for user_num in range(number_of_users):
            Service.objects.create(
                name= f"Servicio {user_num}",
                status= f"active",
                description= f"servicio de prueba descripcion :{user_num}",
                price=random.randint(3000,16000) * user_num
            )
    def test_view_url_exists_at_desired_location(self):
        "Test endpoint users method GET"
        print("Test endpoint users method GET")
        resp = self.client.get('/api/services/')
        print("RESPONSE:", resp)
        self.assertEqual(resp.status_code, 200)

    def test_create_services_in_post_method(self):
        print("Test method post and create service")

        data_send =    {
            "name": "servicio de prueba creado con post",
            "status": "active",
            "description": "descripcion de servicio en testeo",
            "price": 12000
        }
        resp = self.client.post(reverse("service_list"),data_send)
        self.assertEqual(resp.status_code, 201)
        data_json = resp.json()['data']
        self.assertEqual(data_json['price'], 12000)
        self.assertEqual(data_json['name'], "servicio de prueba creado con post")
        self.assertEqual(data_json['description'], "descripcion de servicio en testeo")
