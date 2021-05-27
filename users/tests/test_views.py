from django.test import TestCase
from django.urls import reverse
from users.models import *
from django.contrib.auth.models import User

class UserRegisterTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user ={
            'username' : 'TestUser',
            'email' : 'test@gmail.com',
            'first_name' : 'Test1',
            'last_name' : 'Test2',
            'password1' : 'pass12345',
            'password2' : 'pass12345'
        }
        
        return super().setUp()
        
    def test_user_register(self):
        response = self.client.post(self.register_url,self.user, format = 'text/html')
        self.assertEqual(response.status_code, 302)
    
    def test_user_login(self):
        response = self.client.post(self.register_url,self.user, format = 'text/html')
        response = self.client.post(self.login_url, {'username' : 'TestUser', 'password':'pass12345'}, format = 'text/html')
        self.assertEqual(response.status_code, 302)
        