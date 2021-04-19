# from app import app
import urllib.request, json
from .models import News, NewsSource
from datetime import datetime

today = datetime.today().strftime('%Y-%M-%D')

# News = news.News
# NewsSource = news_source.NewsSource

#Getting api key
apiKey = None


#Getting the news api base url 
base_url = None
source_url = None

def configure_request(app):
    global api_key, base_url, source_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    source_url = app.config['NEWS_SOURCE_BASE_URL']

def get_news(category):
    '''
    Function that takes in the news everything api and returns a json response
    '''
    get_news_details = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_details) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_results = None 

        if news_details_response['articles']:
            news_results_list = news_details_response['articles']
            news_results = process_results(news_results_list)

    return news_results 

def process_results(news_list):
    '''
    Function that processes the sources result and transforms it to a list of objects

    Args:
    sources_list: A list of dictionaries that contain source details

    Returns:
    sources_results: A list of sources objects
    '''

    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        author = news_item.get('author')
        title  = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        if urlToImage:
            news_object = News(id, name, author, title, description, url, urlToImage, publishedAt, content)
            news_results.append(news_object)

    return news_results


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = source_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None
        final_results = []

        if get_sources_response['sources']:
            sources_results = get_sources_response['sources']

        for source_item in sources_results:
            id = source_item.get('id')
            name = source_item.get('name')
            description = source_item.get('description')
            url = source_item.get('url')
            category = source_item.get('category')
            language = source_item.get('language')
            country = source_item.get('country')

            sources_object = NewsSource(id, name, description, url, category, language, country)
            final_results.append(sources_object)

        return final_results

def search_news(news_title):
    search_news_url = 'https://newsapi.org/v2/everything?q={}&language=en&apiKey={}'.format(news_title,api_key)

    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response =json.loads(search_news_data)

        search_news_results = None

        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_movie_results = process_results(search_news_list)

    return search_news_results

