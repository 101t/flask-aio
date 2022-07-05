from flask import request, url_for, Blueprint, jsonify
from flask import current_app

core_views = Blueprint('core_views', __name__)

def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

@core_views.route("/health_check", methods=["GET"])
def health_check():
    version = current_app.config["VERSION"]
    return jsonify({"version": version})


@core_views.route("/", methods=["GET"])
def welcome():
    return '<div align="center"><h1>Welcome to Flask AIO App</h1><p>This only welcome message you could remove it and start your development</p></div>'


