from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from routes import web as web_blueprint
    app.register_blueprint(web_blueprint)
    from routes_api import api as api_blueprint
    app.register_blueprint(api_blueprint)
    
    return app