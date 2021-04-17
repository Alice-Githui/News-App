from flask import render_template
from app import app
from .request import get_sources, get_news

#Views/Routes to our apps
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    sports = get_news('sports')
    headlines = get_news('headlines')
    technology = get_news('technology')
    general = get_news('general')
    beauty = get_news('beauty')
    entertainment = get_news('entertainment')
    trending = get_news('trending')
    sources = get_sources()

    title = "Welcome to the Daily News App. Catch the day\'s news all in one place"

    return render_template('index.html', title= title, sports=sports, headlines= headlines, technology=technology, general=general, beauty=beauty, entertainment= entertainment, trending=trending, sources=sources)

