from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class AccountTests(APITestCase):

    # the setUp method will be called before all test method in the TestClass
    # the teaDown method will be called after all the test method in the TestClass called.
    def setUp(self) -> None:
        # You create a new user in db for testing login and logout. It's not nessessary for the test_register method
        self.user = User.objects.create_user(
            username="user1",
            password="Password123!!!"
        )
    
    def test_login(self):
        # We need the data of the user the login -> you can imagine in the realworld. You login into the facebook page, you have to enter the username and password. It's the same with that case.
        data = {
            "username": "user1",
            "password": "Password123!!!"
        }

        url = reverse('login')

        # send a post login requets with the data like above to the server
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        url = reverse('logout')

        # the first things: you need to get the token of the current use
        # each token has the relationship 1: 1 with user, so we can get the token of the user through the username. >>> user__username
        self.token = Token.objects.get(user__username='user1')
        # Include an appropriate `Authorization:` header on all requests.
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

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


