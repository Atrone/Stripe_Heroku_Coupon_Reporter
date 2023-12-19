from flask_mail import Mail
from flask_stripe import Stripe

stripe_config = Stripe()
mail = Mail()