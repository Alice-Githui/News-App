from flask import Flask   
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

#initializing our application
def create_app(config_name):
    app = Flask(__name__)

    #set up configurations
    app.config.from_object(config_options[config_name])

    #initialize bootstrap
    bootstrap.init_app(app)

    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from .request import configure_request
    configure_request(app)

    return app