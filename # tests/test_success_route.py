

import unittest
from app import app
from unittest.mock import patch, MagicMock

class TestSuccessPage(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    @patch("app.Booking")
    @patch("app.generate_qr")
    def test_success_page_ok(self, mock_qr, mock_booking):
        fake_booking = MagicMock()
        fake_booking.name = "Ahmed"
        fake_booking.booking_id = "B123"
        fake_booking.room_type = "Deluxe"
        fake_booking.total = 5000
        fake_booking.check_in = "2025-01-01"
        fake_booking.check_out = "2025-01-05"

        mock_booking.query.filter_by.return_value.first.return_value = fake_booking
        mock_qr.return_value = "FAKE_QR_DATA"

        response = self.client.get("/success/B123")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Ahmed", response.data)
