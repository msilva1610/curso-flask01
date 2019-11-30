# coding: utf-8
def load(app):
    from app.home import home
    app.register_blueprint(home)