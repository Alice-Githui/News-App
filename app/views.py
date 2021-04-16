from flask import render_template
from app import app

#Views/Routes to our apps
@app.route('/')
def index():
    '''
    View the root page that returns the index page and its data/contents
    '''

    title = 'Welcome to the Daily News App. Catch the day\'s news all in one place'
    message = 'Welcome to this app'
    return render_template('index.html', title = title, message = message)