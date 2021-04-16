from app import app
import urllib.request, json
from .models import news

News = news.News

#Getting api key
apiKey = app.config['NEWS_API_KEY']

#Getting the news api base url 
base_url = app.config["NEWS_API_BASE_URL"]
print(base_url)

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category, apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
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
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        if url:
            news_object = News(id, name, description, url, category, language, country)
            news_results.append(news_object)

    return news_results