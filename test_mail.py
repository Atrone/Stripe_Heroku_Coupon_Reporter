import unittest
from app import create_app
from app.email_services import send_email


class TestEmailService(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_send_email(self):
        self.assertIsNotNone(self.app.config.get('MAIL_USERNAME'))
        self.assertIsNotNone(self.app.config.get('MAIL_PASSWORD'))

        subject = 'Test Email'
        sender = self.app.config.get('MAIL_USERNAME')
        coupons = [{'id': 'COUPON123', 'timestamp': '2021-12-31T23:59:59Z'}]
        recipients_data = {"anthony.teixeira55@gmail.com": coupons}

        with self.app.app_context():  
           response = send_email(subject, sender, recipients_data)
           self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
