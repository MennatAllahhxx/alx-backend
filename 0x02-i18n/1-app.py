#!/usr/bin/env python3
"""
Basic Flask app with babel
"""

from flask import Flask, render_template
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
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
