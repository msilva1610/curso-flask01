# coding: utf-8
from flask import Flask, request, Response
import routes
def bootstrap():
    # from .routes import load
    app = Flask(__name__)
    routes.load(app)
    return app

app = bootstrap()
app.run(debug=True, port=3000, host='0.0.0.0')