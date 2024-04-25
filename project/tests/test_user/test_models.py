"Testing"
from django.test import TestCase
from ...models.models_user import User

# Create your tests here.

class UserTest(TestCase):
    def setUp(self):
        print("create user")
        User.objects.create(
            firstname= "Prueba",
            lastname= "Oyoola",
            password= "password_de_prueba",
            email= "nicooyola@gmail.com",
            birthdate= "1995-09-16"
        )

    def test_verify_user(self):
        """The user with a same email"""
        user_test = User.objects.get(firstname="Prueba")
        self.assertEqual(user_test.email, 'nicooyola@gmail.com')
