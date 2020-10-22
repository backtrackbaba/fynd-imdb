from django.test import TestCase, Client

from django.urls import reverse

client = Client()


class APITestCase(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_api_home(self):
        response = client.get(reverse('api_home'))
        self.assertEqual(response.status_code, 200)
