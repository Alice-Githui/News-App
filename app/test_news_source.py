import unittest
from model_s import news_source   

NewsSource = news_source.NewsSource

class NewsSourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News Source class
    '''

    def setUp(self):
        '''
        set up method that runs before every test
        '''
        self.new_news_source = NewsSource("Reuters","LifeHacker","What You Need to Know About Buying Cryptocurrency on PayPal","https://lifehacker.com/what-you-need-to-know-about-buying-crypt-on-pa-1846585705","Business", "English", 'US')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_source, NewsSource))

if __name__ == '__main__':
    unittest.main()   