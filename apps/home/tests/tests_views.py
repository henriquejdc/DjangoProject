from django.test import TestCase
from django.urls import reverse


class HomeViewTestCase(TestCase):

    def test_status_code_200(self):
        response = self.client.get(reverse('home:home_view'))
        self.assertEqual(response.status_code, 200)
