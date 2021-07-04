from django.test import TestCase
import json
from django.urls import reverse
from . models import ShipData
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.


class ShipListTestCase(APITestCase):
    list_url = reverse("ship-list")

    def test_ship_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ship_detail(self):
        response = self.client.get(reverse("ship-detail", kwargs={"imo": "96321791"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)