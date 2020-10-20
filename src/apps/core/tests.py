from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse

client = Client()


class ViewTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_home_view(self) -> None:
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
