from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    
    def test_create_user_with_email_succesfully(self):
        """Test creating a user with an email is succesfully created"""
        email = "test@gmail.com"
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))