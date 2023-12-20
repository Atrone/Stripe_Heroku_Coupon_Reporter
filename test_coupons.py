import unittest
from app import create_app
from app.stripe_services import fetch_used_coupons

class TestCoupons(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_fetch_used_coupons(self):
        used_coupons = fetch_used_coupons()
        self.assertIsInstance(used_coupons, list)

if __name__ == '__main__':
    unittest.main()