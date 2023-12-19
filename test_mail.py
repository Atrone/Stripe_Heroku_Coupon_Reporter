from app import create_app
from app.email_services import send_email

# Create app
app = create_app()

# Manually push an application context
with app.app_context():
    coupons = [{'id': '1', 'timestamp': '2022-12-01T00:00:00Z'}, {'id': '2', 'timestamp': '2022-12-01T00:01:00Z'}]
    send_email('Test Email', 'app.email@gmail.com', ['test@example.com'], coupons)