# coding: utf-8
from flask import jsonify
from . import home

@home.route('/home')
def index():
    # return dict(title='Home Page', path='/', status_code=200)
    return jsonify(dict(title='Home Page', path='/', status_code=200))