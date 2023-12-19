from flask import current_app
from stripe.error import AuthenticationError
import stripe 
from datetime import datetime, timedelta
import time

def fetch_used_coupons():
    try:
        end = datetime.now()
        start = end - timedelta(minutes=5)

        start_in_unix = int(time.mktime(start.timetuple()))
        end_in_unix = int(time.mktime(end.timetuple()))

        stripe.api_key = current_app.config['STRIPE_SECRET_KEY']

        params = {
            'created': {
                'gte': start_in_unix,
                'lte': end_in_unix
            },
            'type': 'coupon.updated',
        }

        events = stripe.Event.list(**params)
        used_coupons = []
        for event in events.auto_paging_iter():
            coupon = event.data.object
            if not coupon.valid and coupon.redeem_by >= start and coupon.redeem_by <= end:
                used_coupons.append({
                    'id': coupon.id,
                    'timestamp': datetime.fromtimestamp(event.created).strftime('%Y-%m-%dT%H:%M:%SZ')
                })

        return used_coupons
    except AuthenticationError:
        return {'error': 'Stripe API Key not found or invalid.'}
    except Exception as e:
        return {'error': str(e)}