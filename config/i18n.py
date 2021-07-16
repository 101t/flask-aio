from flask import Flask, Blueprint, session, redirect, url_for
from flask import current_app


LANGUAGES = {
    'en': 'English',
    'tr': 'Turkish',
    'ar': 'Arabic',
}

i18n_views = Blueprint('i18n_views', __name__)


@i18n_views.route('/i18n/<lang>', )
def set_language(lang=None):
    session['language'] = lang
    return redirect('/')


