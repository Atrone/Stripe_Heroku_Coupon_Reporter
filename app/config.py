import os

class Config(object):
    STRIPE_SECRET_KEY = os.environ.get('STRIPE')
    MAIL_SERVER = os.environ.get('MAILERTOGO_SMTP_HOST')
    MAIL_PORT = os.environ.get('MAILERTOGO_SMTP_PORT', 587)
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAILERTOGO_SMTP_USER')
    MAIL_PASSWORD = os.environ.get('MAILERTOGO_SMTP_PASSWORD')