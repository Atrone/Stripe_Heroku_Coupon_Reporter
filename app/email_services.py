from flask_mail import Message
from flask import current_app, render_template
from .extensions import mail


def send_email(subject, sender, recipients_data):
    for recipient, coupons in recipients_data.items():
        msg = Message(subject, sender=sender, recipients=[recipient])
        if coupons:  # If there are coupons for current recipient
            msg.html = render_template('email_report.html', coupons=coupons)
            mail.send(msg)
        else:  # If there are no coupons for the current recipient
            msg.html = 'There are no assigned coupons!'
