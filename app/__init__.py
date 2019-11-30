# coding: utf-8
from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from config import config


db = SQLAlchemy()

# import routes
def create_app(config_name):
    # from .routes import load
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)

    from app import routes  
    routes.load(app)
    return app

# app = bootstrap()
# app.run(debug=True, port=3000, host='0.0.0.0')