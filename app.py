# coding: utf-8
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello home!!!'

app.run(debug=True, port=3000, host='0.0.0.0')