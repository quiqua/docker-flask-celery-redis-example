
from flask import Flask

from .extensions import celery

import logging



def create_app():
    app = Flask(__name__)
    app.config.update(CELERY_BROKER_URL="redis://redis")
    app.config.update(CELERY_RESULT_BACKEND="redis://redis")
    create_extensions(app)
    register_blueprints(app)
    return app


def create_extensions(app):
    celery.init_app(app)


def register_blueprints(app):
    from .views import api
    app.register_blueprint(api)


def configure_logging(app):
    # Log only in production mode.
    if not app.debug:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(stream_handler)