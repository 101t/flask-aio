from config.settings import initialize_app


def create_app():
    return initialize_app(config="config.settings.FlaskConfigPro")
