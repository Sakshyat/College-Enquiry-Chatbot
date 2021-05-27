from django.test import TestCase
from herald.views import *

class ListViewTest(TestCase):
    def setUp(self):
        self.view = PostListView()
        
    def test_review_list(self):
        self.assertEqual(self.view.model, Review)
        self.assertEqual(self.view.context_object_name, 'reviews')
        self.assertEqual(self.view.template_name, 'herald/review.html')
        
class CreateViewTest(TestCase):
    def setUp(self):
        self.view = PostCreateView()
        
    def test_review_create(self):
        self.assertEqual(self.view.model, Review)
        self.assertTrue(self.view.form_valid)
        
class UpdateViewTest(TestCase):
    def setUp(self):
        self.view = PostUpdateView()
        
    def test_review_update(self):
        self.assertEqual(self.view.model, Review)
        self.assertTrue(self.view.form_valid)
        self.assertTrue(self.view.test_func)

class DeleteViewTest(TestCase):
    def setUp(self):
        self.view = PostDeleteView()
        
    def test_review_delete(self):
        self.assertEqual(self.view.model, Review)
        self.assertTrue(self.view.get_success_url)
        self.assertTrue(self.view.test_func)