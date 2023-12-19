# Stripe_Heroku_Coupon_Reporter

## Summary
The software application named Stripe_Heroku_Coupon_Reporter fetches and reports on used Stripe coupons. Integrating with a Heroku backend, the application runs a job every 5 minutes which fetches any coupons used from the Stripe dashboard and generates an email report of these coupons, including information like the coupon's ID and when it was used. 

## Technology Stack
This application makes use of the following technologies:
- Python
- Flask
- Stripe API
- Flask-Mail
- HTML
- CSS3
- Bootstrap
- Jinja2 Templates
- Heroku Scheduler
- Requests

## File Structure
- app/extensions.py: Defines and configures the Flask-Mail and Stripe API instances
- app/__init__.py: Configures and initializes the Flask application
- app/stripe_services.py: Responsible for fetching and processing data from the Stripe API
- app/templates/email_report.html: Defines the HTML template used for the coupon report emails
- app/tasks.py: Manages the emailing of coupon report emails
- test.py: Used for testing the Stripe API service
- run.py: Entry point to the application

## Installation and Usage
1. Ensure Python environment is set up and install the requirements from `requirements.txt` file.
2. You must also set up a `.env` file, which should include your `STRIPE_SECRET_KEY`.
3. Start the Flask server using `run.py`. 
4. Test the fetching of used coupons with the `/test.py`.

The coupons used within the last 5 minutes will be fetched from Stripe and an email report will be sent.

Please refer to individual comments within files for more details.