from app import app
import urllib.request, json
from .models import news
from .model_s import news_source

News = news.News

#Getting api key
apiKey = app.config['NEWS_API_KEY']

#Getting the news api base url 
base_url = app.config["NEWS_API_BASE_URL"]
source_url = app.config["NEWS_SOURCE_BASE_URL"]
print(base_url)

def get_sources(category):
    '''
    Function that gets the json response to the news sources request
    '''
    get_sources_url = source_url.format(category, apiKey)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results_list = process_results(sources_results_list)

    return sources_results

def process_results(sources_list):
    '''Function that processes th sources results and transforms them to a list of objects

    Args:
    sources_list: A list of dictionaries that contain the sources details

    Returns:
    sources_results: A list of source article objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if url:
            source_object = NewsSource(id, name, description, url, category, language, country)
            sources_results.append(source_object)

    return sources_results


def get_news(category,query):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,query,apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    '''
    Function that processes the news results and transforms them to a list of objects
    
    Args:
    news_list: A list of dictionaries that contain news article details

    Returns:
    news_results: A list of news article objects
    '''
    news_results = []
    for news_item in news_list:
        source = news_item.get('source')
        # name = news_item.get('source.name')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')
       

        if urlToImage:
            news_object = News(source, author, title, description, url, urlToImage, publishedAt, content)
            news_results.append(news_object)

    return news_results