from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

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
        self.assertEqual(user.user_type,1)

class SignUpPageTests(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('signup'))

    def test_signup_template(self):
        self.assertEqual(self.respone.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')