# Stripe_Heroku_Coupon_Reporter

## Overview

The Stripe_Heroku_Coupon_Reporter is a software application designed to fetch and report used Stripe coupons. The application runs a job every 5 minutes on a Heroku backend, fetching the used coupons and collating an email report. The contents of the report include each coupon's timestamp and ID.

The email reports are generated using Gmail, formatted in HTML, and distributed to multiple recipients. The recipients' specifics are yet to be determined.

## Technology Stack

The application leverages several technologies including:

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

## Setup

1. Install the requirements: Ensure Python environment is set up and then install the requirements from `requirements.txt`

2. Create a `.env` file and set up your `STRIPE_SECRET_KEY`

3. Run `run.py` to start the Flask server

4. The server fetches coupon data from Stripe every 5 minutes and sends a report.

## Usage

Run `/test.py` to test fetching of used coupons. To test the email functionality, use `/test_mail.py` which creates an email with dummy coupon data.

## File Overview

- `app/extensions.py`: Initializes Flask-Mail and Stripe

- `app/__init__.py`: Creates and configures the Flask app

- `app/stripe_services.py`: Fetches used coupons from Stripe API

- `app/templates/email_report.html`: HTML template for the email report

- `app/email_services.py`: Sets up the structure and sends the emails

- `run.py`: Entry point for running the app

## Additional Info

Recipients of the email reports are to be determined in further stages of the project.

Ensure compliance with Stripe's API guidelines while using Stripe_Heroku_Coupon_Reporter.
