from flask import current_app
from .stripe_services import fetch_used_coupons
from .email_services import send_email

def send_report():
    with current_app.app_context():
        used_coupons = fetch_used_coupons()
        if 'error' in used_coupons:
            print(f"Error occurred: {used_coupons['error']}")
            return
        subject = "Used Coupons Report"
        sender = current_app.config['MAIL_USERNAME']
        recipients = ["anthony.teixeira55@gmail.com"]
        send_email(subject, sender, recipients, used_coupons)