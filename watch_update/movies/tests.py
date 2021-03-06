from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate

from movies.api import serializers
from movies import models


class StreamPlatformTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="admin1",
            password="Password!!!123"
        )
        self.token = Token.objects.get(user__username="admin1")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.url = reverse('streamplatform-list')

        self.stream = models.StreamPlatform.objects.create(
            name="name1",
            about="about1",
            website="https://website.com",            
        )

    def test_create_streamplatform(self):
        data = {
            "name": "name1",
            "about": "about1",
            "website": "https://website.com",
        }

        # because this class view is inherit from ViewSet. So from basename we need add the -list to the test determine the exactly routename
        # url = reverse('streamplatform-list')

        response = self.client.post(self.url, data)
        # permission_classes = [IsAdminOrReadOnly] in the StreamPlatformViewSet
        # so we need setUp to the current user sent request is the admin to pass the authorize
        # the user in the setUp method isn't the admin user -> so they cannot create, update or delete the streamplatform
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_all_streamplatform(self):
        # streamplatform: is the baseroutename -> if you want to call get list -> you using the partten: <baseroutename>-list
        url = reverse('streamplatform-list')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_specific_streamplatform(self):
        # streamplatform: is the baseroutename -> if you want to retrieve specific item -> you using the partten: <baseroutename>-detail. That is the reason why the below url is: streamplatform-detail
        url = reverse('streamplatform-detail', args=(self.stream.id, ))
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WatchListTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="admin1",
            password="Password!!!123"
        )
        self.token = Token.objects.get(user__username="admin1")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.url = reverse('watchlist_list')
        self.streamplatform = models.StreamPlatform.objects.create(
            name="name1",
            about="about1",
            website="https://website.com",            
        )
        self.watchlist = models.WatchList.objects.create(
            title="watchlist1",
            storyline="this is the storyline of the watchlist1",
            stream_platform=self.streamplatform,
            active=True,            
        )

    def test_create_watchlist(self):
        data = {
            "title": "watchlist1",
            "storyline": "this is the storyline of the watchlist1",
            "stream_platform": self.streamplatform,
            "active": True,
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def tets_get_all_watchlist(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_specific_watchlist(self):
        url = reverse('watchlist_detail', args=(self.watchlist.id, ))
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)  
        self.assertEqual(models.WatchList.objects.count(), 1)  
        self.assertEqual(models.WatchList.objects.get().title, "watchlist1")  


class ReviewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="admin1",
            password="Password!!!123"
        )
        self.token = Token.objects.get(user__username="admin1")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.streamplatform = models.StreamPlatform.objects.create(
            name="name1",
            about="about1",
            website="https://website.com",            
        )
        self.watchlist = models.WatchList.objects.create(
            title="watchlist",
            storyline="this is the storyline of the watchlist",
            stream_platform=self.streamplatform,
            active=True,            
        )
        self.watchlist1 = models.WatchList.objects.create(
            title="watchlist1",
            storyline="this is the storyline of the watchlist1",
            stream_platform=self.streamplatform,
            active=True,            
        )
        self.review = models.Review.objects.create(
            author=self.user,
            rating=5,
            description="Good movie",
            watchlist=self.watchlist,
            active=True,
        )

    def test_create_review_with_authorized(self):
        url = reverse('review_create', args=(self.watchlist1.id, ))
        data = {
            "author": self.user,
            "rating": 5,
            "description": "Good movie",
            "watchlist": self.watchlist1,
            "active": True,            
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Review.objects.count(), 2) 

    def test_create_review_with_unauthorized(self):
        self.client.force_authenticate(user=None, token=None)
        url = reverse('review_create', args=(self.watchlist1.id, ))
        data = {
            "author": self.user,
            "rating": 5,
            "description": "Good movie",
            "watchlist": self.watchlist1,
            "active": True,            
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_get_all_review(self):
        url = reverse('review_list', args=(self.watchlist1.id, ))
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_specific_review(self):
        url = reverse('review_detail', args=(self.review.id, ))
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_review(self):
        data = {
            "author": self.user,
            "rating": 4,
            "description": "Good movie! - updated",
            "watchlist": self.watchlist1,
            "active": False,
        }
        url = reverse('review_detail', args=(self.review.id, ))
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_review_list(self):
        url = f"{reverse('user_review_list')}?username={self.user.username}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)