#!/usr/bin/env python3
"""
Basic Flask app with babel
"""

from flask import Flask, render_template, request
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


@app.route('/')
def index():
    """AI is creating summary for index

    Returns:
        str: html template
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """AI is creating summary for get_locale
    """
    if (request.args.get('locale')) and\
       (request.args.get('locale') in app.config['LANGUAGES']):
        return request.args.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
