from flask import Flask
from .extensions import stripe_config, mail
from .config import Config
from flask.cli import AppGroup
from .tasks import send_report

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    stripe_config.init_app(app)
    mail.init_app(app)

    report_cli = AppGroup('report')

    @report_cli.command('send')
    def send_report_cmd():
        send_report()

    app.cli.add_command(report_cli)
    return app