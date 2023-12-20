import unittest
from unittest.mock import patch

from app.stripe_services import Coupon
from app.tasks import send_report
from app import create_app

class SendReportTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    @patch('app.tasks.fetch_used_coupons')
    @patch('app.tasks.send_email')
    def test_send_report(self, mock_send_email, mock_fetch_used_coupons):
        mock_fetch_used_coupons.return_value = [
            Coupon(**{'id': 'coupon_1', 'timestamp': '2022-12-01T00:00:00Z'}),
            Coupon(**{'id': 'coupon_2', 'timestamp': '2022-12-02T00:00:00Z'}),
        ]
        send_report()
        mock_send_email.assert_called_once()
        call_args = mock_send_email.call_args[0]
        self.assertEqual(call_args[0], 'Used Coupons Report')
        self.assertEqual(call_args[1], self.app.config['MAIL_USERNAME'])

        recipient, coupons = list(call_args[2].items())[0]
        self.assertEqual(recipient, 'anthony.teixeira55@gmail.com')
        self.assertEqual(len(coupons), 1)
        self.assertEqual(coupons[0].id, 'coupon_1')

if __name__ == '__main__':
    unittest.main()