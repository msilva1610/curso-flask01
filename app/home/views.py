# coding: utf-8
from . import home

@home.route('/home')
def index():
   return 'Home Page'