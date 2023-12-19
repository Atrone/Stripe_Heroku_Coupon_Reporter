from app import create_app
from app.stripe_services import fetch_used_coupons

# Create app
app = create_app()

# Manually push an application context
with app.app_context():
    used_coupons = fetch_used_coupons()
    print(used_coupons)