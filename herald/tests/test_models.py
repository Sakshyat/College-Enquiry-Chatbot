from django.test import TestCase
from herald.models import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class TestModel(TestCase):
    def setUp(self):
        self.review_url = reverse('herald-review')
        self.user = User.objects.create(username = 'TestUser')
     
    def test_model(self):
        self.review = Review.objects.create(
        content = 'Test Content',
        date_posted = timezone.now(),
        author = self.user
        )
        self.assertEqual(self.review.__str__(), 'Test Content')
        self.assertEqual(self.review.get_absolute_url(), self.review_url)
        