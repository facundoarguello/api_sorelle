from django.test import TestCase

# Create your tests here.

from project.models import User
from django.urls import reverse

class UserViewTest(TestCase):

    def setUpTestData(self):
        number_of_users = 15
        for user_num in range(number_of_users):
            User.objects.create(
                firstname= f"Rodolgo {user_num}",
                lastname= f"Arguello {user_num}",
                password= f"passworddeprueba{user_num}",
                email= f"Rodimail{user_num}@gmail.com",
                birthdate= "1975-11-25"
            )
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/api/users/')
        self.assertEqual(resp.status_code, 200)