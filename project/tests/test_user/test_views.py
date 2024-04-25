from django.test import TestCase
import random
import json
# Create your tests here.

from ...models.models_user import User
from django.urls import reverse

class UserViewTest(TestCase):

    def setUp(self):
        
        number_of_users = 15
        for user_num in range(number_of_users):
            User.objects.create(
                firstname= f"Rodolgo {user_num}",
                lastname= f"Arguello {user_num}",
                password= f"passworddeprueba{user_num}",
                email= f"Rodimail{user_num}@gmail.com",
                role="normal",
                birthdate= "1975-11-25"
            )
    def test_view_url_exists_at_desired_location(self):
        "Test endpoint users method GET"
        resp = self.client.get('/api/users/')
        print("RESPONSE:", resp)
        self.assertEqual(resp.status_code, 200)

    def test_view_pagination(self):
        "Test pagination in endpoint users method GET"
        resp = self.client.get(reverse('user_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()['data']), 5)
    def test_one_user_post(self):
        "Test insert one user in bd on endpoint users METHOD POST"
        number = random.randint(10,1000)
        obj_user = {

            "firstname": "Milagros",
            "lastname": "Oyoola",
            "password": f"One_Piece_{number}_Mila",
            "email": "miliarguello@gmail.com",
            "birthdate": "1985-04-10"
        }
        pass_word_equal = f"One_Piece_{number}_Mila"
        resp = self.client.post(reverse('user_list'),obj_user)
        self.assertEqual(resp.status_code, 201)
        data = resp.json()['data']
        print(data)
        self.assertEqual(data['password'], pass_word_equal)
        self.assertEqual(data['firstname'], 'Milagros')
    
    def test_one_user_put(self):
        "Test insert one user in bd on endpoint users METHOD PUT"
        user_obj = {
            "firstname": "Licho",
            "lastname": "Arguello",
            "password": "passworddeprueba",
            "email": "cr7@gmail.com",
            "birthdate": "1995-02-22",
            "status": 'active',
            "role": "normal"
        }
        user_test = User.objects.create(**user_obj)
        self.assertEqual(user_test.email, 'cr7@gmail.com')
        self.assertEqual(user_test.password, 'passworddeprueba')
        pk = user_test.id
        url = reverse('user_list') + f'?pk={pk}'
        print(user_test.lastname)
        #change data in object user
        user_obj['lastname'] = 'De La Cruz'
        user_obj['password'] = 'cr7_el_mejor'
        print("put", url)
        user_obj_dump = json.dumps(user_obj)
        resp = self.client.put(url,user_obj_dump, content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        data = resp.json()['data']
        print("put",data)
        self.assertEqual(data['lastname'], 'De La Cruz')
        self.assertEqual(data['password'], 'cr7_el_mejor')
    
    def test_one_user_delete(self):
        "Test DELETE A USER  "
        user_obj = {
            "firstname": "Pancho",
            "lastname": "Arguello",
            "password": "passworddeprueba",
            "email": "cr7@gmail.com",
            "birthdate": "1995-02-22",
            "status": 'active',
            "role": "normal"
        }
        name_view_url = reverse('user_list')
        user_test = User.objects.create(**user_obj)
        pk = user_test.id
        url_del =name_view_url + f'?pks={pk}'
        print("delete", url_del)
        resp = self.client.delete(url_del)
        self.assertEqual(resp.status_code, 204)



        
