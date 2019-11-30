def load(app):
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