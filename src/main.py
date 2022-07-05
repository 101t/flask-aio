from distutils.log import debug
from config.settings import initialize_app

import os


FLASK_CONFIG = os.getenv("FLASK_CONFIG", default="config.settings.FlaskConfigDev")

def create_app():
    return initialize_app(config=FLASK_CONFIG)

if __name__ == "__main__":
    app = create_app()
    app.run()
