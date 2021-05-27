from django.test import SimpleTestCase
from django.urls import reverse, resolve
from herald.views import *

class TestUrls(SimpleTestCase):
    def test_home(self):
        url = reverse('herald-home')
        self.assertEquals(resolve(url).func, home)
    
    def test_review(self):
        url = reverse('herald-review')
        self.assertEquals(resolve(url).func.view_class, PostListView)
        
    def test_create_post(self):
        url = reverse('create-post')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)
    
    def test_update_post(self):
        url = reverse('update-post', args = ['1'])
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)
   
    def test_delete_post(self):
        url = reverse('delete-post', args = ['1'])
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)