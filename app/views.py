from flask import render_template
from app import app

#Views/Routes to our apps
@app.route('/')
def index():
    '''
    View the root page that returns the index page and its data/contents
    '''
    return render_template('index.html')