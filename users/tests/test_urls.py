from django.test import TestCase
from django.urls import reverse

class UserRegisterTest(TestCase):
        
    def test_register_url(self):
        self.register_url = reverse('register')
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_login_url(self):
            self.login_url = reverse('login')
            response = self.client.get(self.login_url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'users/login.html')
            