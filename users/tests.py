from django.test import TestCase

from django.contrib.auth import get_user_model

# Create your tests here.

class CustomUserTests(TestCase):
    def test_create_user(self):

        User = get_user_model()
        user = User.objects.create_user(
            username='will',
            email='will@email.com',
            password='testpass123',
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email.com')
