from flask import render_template, request, redirect,url_for
from .import main
from ..request import get_sources, get_news, search_news

#Views/Routes to our apps
@main.route('/')
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

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('main.search', news_title=search_news))
    else: 
        return render_template('index.html', title= title, sports=sports, headlines= headlines, technology=technology, general=general, beauty=beauty, entertainment= entertainment, trending=trending, sources=sources)

@main.route('/search/<news_title>')
def search(news_title):
    '''
    View function to display the search results
    '''
    news_title_list = news_title.split(" ")
    news_title_format = "+".join(news_title_list)
    searched_news = search_news(news_title_format)
    title = f'search results for {news_title}'
    message = 'Hello World'
    return render_template('search.html', news = searched_news, message=message)
