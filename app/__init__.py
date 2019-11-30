# coding: utf-8
from flask import Flask, request, Response
# import routes
def create_app():
    # from .routes import load
    app = Flask(__name__)
    from app import routes
    routes.load(app)
    return app

# app = bootstrap()
# app.run(debug=True, port=3000, host='0.0.0.0')