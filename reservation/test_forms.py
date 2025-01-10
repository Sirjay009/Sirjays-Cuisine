from django.test import TestCase
from .forms import ReservationForm


class TestReservationForm(TestCase):

    def test_form_is_valid(self):
        """Test for all fields"""
        form = ReservationForm({
            "name": "John Doe",
            "user": "user",
            "email": "johndoe@example.com",
            "phone": "1234567890",
            "guests": 4,
            "reservation_date": "2025-01-15",
            "reservation_time": "18:30:00",
            "special_request": "Window seat"
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_form_is_invalid(self):
        """Test for invalid fields"""
        form = ReservationForm({
            "name": "",
            "user": "",
            "email": "",
            "phone": "",
            "guests": "",
            "reservation_date": "",
            "reservation_time": "",
            "special_request": ""
        })
        self.assertFalse(form.is_valid(), msg="Form is valid")
