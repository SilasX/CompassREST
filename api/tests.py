import json

from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

# Using the standard RequestFactory API to create a form POST request

class TestProducts(APITestCase):

    fixtures = ["seed.json"]

    def setUp(self):
        pass

    def test_product1(self):
        new_name = "zoggy"
        changes = {
            "name": new_name,
        }
        response = self.client.patch('/products/1/', changes)
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/products/1/')
        self.assertEqual(response.status_code, 200)
        self.client.login(username="corp", password="hunter2")
        response = self.client.get('/products/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.patch('/products/1/', changes)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data["name"], new_name)
        self.client.login(username="noncorp", password="hunter2")
        response = self.client.patch('/products/1/', changes)
        self.assertEqual(response.status_code, 403)
