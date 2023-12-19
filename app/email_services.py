from flask_mail import Message
from flask import current_app, render_template
from .extensions import mail


def send_email(subject, sender, recipients, coupons):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.html = render_template('email_report.html', coupons=coupons)
    mail.send(msg)