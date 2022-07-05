"""Flask AIO"""
import os
from flask import Flask, request, jsonify
from main.core import core_views
from version import __VERSION__
import traceback  # error traceback
from werkzeug.exceptions import default_exceptions  # exception handling
from werkzeug.exceptions import HTTPException  # exception handling

ROOT_DIR = os.path.abspath('..')
APPS_DIR = os.path.join(ROOT_DIR, 'main')
CONF_DIR = os.path.join(ROOT_DIR, 'config')

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class FlaskConfigBase(object):
    VERSION = __VERSION__
    DEBUG = bool(os.environ.get('DEBUG', default=True))
    CSRF_ENABLED = bool(os.environ.get('CSRF_ENABLED', default=False))
    SECRET_KEY = os.environ.get('SECRET_KEY', default='my-secret-key')
    HOST = os.environ.get("HOST", default="0.0.0.0")
    PORT = os.environ.get('PORT', default="5000")
    DATABASE_URL = os.environ.get('DATABASE_URL', default='sqlite:///sqlite3.db')
    REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
    QUEUES = ["default"]


class FlaskConfigDev(FlaskConfigBase):
    pass


class FlaskConfigPro(FlaskConfigBase):
    pass


def initialize_app(config="config.settings.FlaskConfigPro"):
    # instantiate the app
    app = Flask(__name__, instance_relative_config=False)
    # set config
    app.config.from_object(obj=config)

    # register blueprints
    app.register_blueprint(core_views)

    # better exception handling
    @app.errorhandler(Exception)
    def handle_error(e):
        # 400 for https error, 500 for internal error
        if isinstance(e, HTTPException):
            # status_code = e.code
            status_code = 400
        else:
            status_code = 500
        # prepare error message
        message = str(e)
        # stdout error traceback
        print(traceback.format_exc())
        # return response
        return jsonify(message=message, error_traceback=traceback.format_exc()), status_code

    for ex in default_exceptions:
        app.register_error_handler(ex, handle_error)

    return app
