from django.test import TestCase
from .models import CustomUser 

class CustomUserModelTest(TestCase):
    def test_create_user(self):
        # Create a user for testing
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')
    