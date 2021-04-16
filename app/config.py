class Config:
    '''
    contains general configuration of parent class
    '''
    pass

class ProdConfig:
    '''
    contains configuration that will be used in production - child class

    Args:
    Config: The parent configiration class with general configuration settings
    '''
    pass

class DevConfig:
    '''
    contains configuration that will be used in development. 

    Args:
    Config: The parent configuartion class with General Configuration settings
    '''
    DEBUG  = True 