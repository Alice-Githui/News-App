from flask import Flask   
from .config import DevConfig

#initializing our application
app = Flask(__name__)

#set up configurations
app.config.from_object(DevConfig)

from app import views