from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class UserTests(APITestCase):
    def test_register_user(self):
        """
        Ensure we can create a new user object.
        """
        url = reverse('register')
        data = {
            "username": "username1",
            "email": "email1.example@gmail.com",
            "password": "Password123!!!!",
            "password2": "Password123!!!!"
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



