from flask import Flask   
from .config import DevConfig
from flask_bootstrap import Bootstrap

#initializing our application
app = Flask(__name__,instance_relative_config = True)

#set up configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#initialize bootstrap
bootstrap = Bootstrap(app)

from app import views