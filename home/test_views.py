from django.test import TestCase
from django.urls import reverse
from .models import Home, Menu


class TestHomeViews(TestCase):

    def setUp(self):
        """Set up test data for home"""
        self.home = Home.objects.create(
            title='Title',
            slogan='Slogan'
        )

        self.menu = Menu.objects.create(
            dish='Dish',
            description='Description',
            price='12.00',
            featured_image='image'
        )

        self.home_url = reverse('home')

    def test_render_home_items(self):
        """Verifies GET request for home."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Title', response.content)
        self.assertIn(b'Slogan', response.content)
        self.assertIn(b'Dish', response.content)
        self.assertIn(b'Description', response.content)
