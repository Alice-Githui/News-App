import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        set up method that runs before every test
        '''
        self.new_news = News(1234, "LifeHacker", "The ins and outs of buying cryptocurrency","https://lifehacker.com/what-you-need-to-know-about-buying-crypt-on-pa-1846585705","Business News", "En", "US")


    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

if __name__ == '__main__':
    unittest.main()   