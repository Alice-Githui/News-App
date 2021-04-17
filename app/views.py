from flask import render_template
from app import app
from .request import get_sources, get_news

#Views/Routes to our apps
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting the source list
    var_sources = get_sources('sources')
    print(var_sources)
    title = 'Welcome to the Daily News App. Catch the day\'s news all in one place'
    return render_template('index.html', title=title, sources=var_sources)

@app.route('/news/category')
def news(category):
    '''
    View the news page function that returns the news details page and the data
    '''
    news = get_news(category)
    title = f'{news.title}'

    return render_template('newsarticles.html', title=title, news=news)