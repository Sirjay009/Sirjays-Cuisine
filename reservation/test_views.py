from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import ReservationForm
from .models import Reservation, Page


class TestReservationViews(TestCase):

    def setUp(self):
        """Set up test data for reservation views."""
        self.user = User.objects.create_superuser(
            username='myUsername',
            password='myPassword',
            email='test@test.com'
        )

        self.client.login(username='myUsername', password='myPassword')

        self.reservation = Reservation.objects.create(
            name='Chima',
            user=self.user,
            phone='12345689',
            guests=4,
            reservation_date='2025-01-15',
            reservation_time='18:30:00',
            special_request='Window seat'
        )
        # URL for the reservation view
        self.reservation_url = reverse('reservation')
        self.edit_url = reverse("reservation_edit", args=[self.reservation.id])
        self.delete_url = reverse(
            "reservation_delete", args=[self.reservation.id])

    def test_reservation_view_contains_reservation_form(self):
        """Test that the reservation view includes a ReservationForm."""
        response = self.client.get(self.reservation_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('reservation_form', response.context)
        self.assertIsInstance(
            response.context['reservation_form'], ReservationForm)

    def test_reservation_edit_view_get_request(self):
        """Test that the edit view renders correctly with a GET request."""
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reservation/reservation_edit.html")
        self.assertIsInstance(
            response.context["reservation_form"], ReservationForm)
        self.assertEqual(
            response.context["reservation"].id, self.reservation.id)

    def test_reservation_delete_view(self):
        """Test that a reservation is deleted."""
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("reservation"))

        # Check if the reservation no longer exists
        with self.assertRaises(Reservation.DoesNotExist):
            Reservation.objects.get(id=self.reservation.id)

    def test_successful_reservation_submission(self):
        """Test that a valid POST request creates a new reservation."""
        post_data = {
            "name": "Chima",
            "phone": "12345689",
            "guests": 4,
            "reservation_date": "2025-01-15",
            "reservation_time": "18:30:00",
            "special_request": "Window seat",
        }

        response = self.client.post(reverse("reservation"), data=post_data)

        # Check that the response redirects (status code 302)
        self.assertEqual(response.status_code, 200)

        # Follow the redirect
        response = self.client.get(reverse("reservation"))

        # Check that the reservation was created in the database
        self.assertEqual(Reservation.objects.count(), 1)
        reservation = Reservation.objects.first()

        # Verify the reservation details
        self.assertEqual(reservation.name, "Chima")
        self.assertEqual(reservation.phone, "12345689")
        self.assertEqual(reservation.guests, 4)
        self.assertEqual(str(reservation.reservation_date), "2025-01-15")
        self.assertEqual(str(reservation.reservation_time), "18:30:00")
        self.assertEqual(reservation.special_request, "Window seat")
        self.assertEqual(reservation.user, self.user)


class TestPageViews(TestCase):

    def setUp(self):
        """Creates page content"""
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.client.login(username="testuser", password="password123")

        self.page_items = Page(
            label="Label content",
            banner="Banner content"
        )
        self.page_items.save()

    def test_render_page_items(self):
        """Verifies GET request for page"""
        response = self.client.get(reverse('reservation'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Label content', response.content)
        self.assertIn(b'Banner content', response.content)
