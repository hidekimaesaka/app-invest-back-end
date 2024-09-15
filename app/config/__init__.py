from os import getenv

from flask import Flask

from dotenv import load_dotenv


def load_config(app: Flask):
    load_dotenv()
    app.config["JWT_SECRET_KEY"] = getenv('JWT_SECRET_KEY')
