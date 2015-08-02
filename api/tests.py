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


class TestSellListings(APITestCase):

    fixtures = ["seed.json"]

    def setUp(self):
        pass

    def test_product1(self):
        self.client.login(username="corp", password="hunter2")
        values = {
            "product": 1,
            "dateListed": '2015-08-01T20:02:04.025026',
            "volumeAvailable": 10,
        }
        response = self.client.post('/selllistings/', values)
        self.assertEqual(response.status_code, 201)
        response = self.client.get('/selllistings/')
        # Should be 3 now
        self.assertEqual(3, len(json.loads(response.content)))
        # Reject non-existent values with 400
        values = {
            "product": 30,
            "dateListed": '2015-08-01T20:02:04.025026',
            "volumeAvailable": 10,
        }
        response = self.client.post('/selllistings/', values)
        self.assertEqual(response.status_code, 400)
        # The same for missing fields
        values = {
            "product": 30,
            "volumeAvailable": 10,
        }
        response = self.client.post('/selllistings/', values)
        self.assertEqual(response.status_code, 400)
