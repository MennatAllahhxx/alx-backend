#!/usr/bin/env python3
"""
Basic Flask app with babel
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """AI is creating summary for Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """AI is creating summary for get_locale
    """
    if (request.args.get('locale')) and\
       (request.args.get('locale') in app.config['LANGUAGES']):
        return request.args.get('locale')

    elif g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    elif request.headers['locale'] in app.config['LANGUAGES']:
        return request.headers['locale']

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """AI is creating summary for get_user

    Returns:
        Union[Dict, None]: user dictionary if found otherwise None
    """
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None


@app.before_request
def before_request():
    """AI is creating summary for before_request
    """
    g.user = get_user()


@app.route('/')
def index():
    """AI is creating summary for index

    Returns:
        str: html template
    """
    if g.user:
        username = g.user['name']
    else:
        username = None
    return render_template('6-index.html', username=username)


if __name__ == "__main__":
    app.run()
