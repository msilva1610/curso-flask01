# coding: utf-8
from flask import Flask, request, Response

def bootstrap():
    app = Flask(__name__)

    @app.route('/home')
    def home():
        return 'Home Page', 200
        # return Response ('Home page', 200, {})


    @app.route('/name')
    @app.route('/name/<name>')
    def showname_param(name = None):
        if name:
            return name
        return 'Name não foi preenchido'
    
    return app

app = bootstrap()

app.run(debug=True, port=3000, host='0.0.0.0')