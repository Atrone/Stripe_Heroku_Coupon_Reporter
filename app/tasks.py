from typing import List

from flask import current_app
from .stripe_services import fetch_used_coupons, Coupon
from .email_services import send_email


def send_report():
    with current_app.app_context():
        used_coupons : List[Coupon] = fetch_used_coupons(window_of_minutes=10)
        if not used_coupons:
            print('No Used Coupons')
            return
        subject = "Used Coupons Report"
        sender = current_app.config['MAIL_USERNAME']
        recipients_data = {"anthony.teixeira55@gmail.com": list(filter(lambda x: (x.id in ['coupon_1']), used_coupons))}
        send_email(subject, sender, recipients_data)
