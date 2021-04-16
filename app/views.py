from flask import render_template
from app import app
from .request import get_news

#Views/Routes to our apps
@app.route('/')
def index():
    '''
    View the root page that returns the index page and its data/contents
    '''
    #Getting all news from the api
    source_news = get_news('sources')
    print(source_news)
    title = 'Welcome to the Daily News App. Catch the day\'s news all in one place'
    # message = 'Welcome to this app'
    return render_template('index.html', title = title, sources = source_news)