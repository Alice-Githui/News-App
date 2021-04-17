class Config:
    '''
    contains general configuration of parent class
    '''
    NEWS_API_BASE_URL='https://newsapi.org/v2/{}?q={}&apiKey={}'

    NEWS_SOURCE_BASE_URL='https://newsapi.org/v2/{}apiKey={}'
    
class ProdConfig(Config):
    '''
    contains configuration that will be used in production - child class

    Args:
    Config: The parent configiration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    contains configuration that will be used in development. 

    Args:
    Config: The parent configuartion class with General Configuration settings
    '''
    DEBUG  = True 