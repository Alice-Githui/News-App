from app import app
import urllib.request, json
from .models import news
from .model_s import news_source

News = news.News
NewsSource = news_source.NewsSource

#Getting api key
apiKey = app.config['NEWS_API_KEY']

#Getting the news api base url 
base_url = app.config["NEWS_API_BASE_URL"]
source_url = app.config["NEWS_SOURCE_BASE_URL"]
print(base_url)

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = source_url.format(category, apiKey)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = []

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results

def process_results(sources_list):
    '''
    Function that processes the sources result and transforms it to a list of objects

    Args:
    sources_list: A list of dictionaries that contain source details

    Returns:
    sources_results: A list of sources objects
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
            sources_object = NewsSource(id, name, description, url, category, language, country)
            sources_results.append(sources_object)

    return sources_results

def get_news(category):
    '''
    Function that takes in the news everything api and returns a json response
    '''
    get_news_details = base_url.format(category, apiKey)

    with urllib.request.urlopen(get_news_details) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None  
        if news_details_response:
            id = news_details_response.get('id')
            name = news_details_response.get('name')
            author = news_details_response.get('author')
            title  = news_details_response.get('title')
            description = news_details_response.get('description')
            url = news_details_response.get('url')
            urlToImage = news_details_response.get('urlToImage')
            publishedAt = news_details_response.get('publishedAt')
            content = news_details_response.get('content')

            news_object =  News(id, name, author, title, description, url, urlToImage, publishedAt, content)

    return news_object

        