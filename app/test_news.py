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
        self.new_news = News(1234, "Lifehacker.com", "LifeHacker", "What you need to know about buying cryptocurrency", "The ins and outs of buying cryptocurrency","https://lifehacker.com/what-you-need-to-know-about-buying-crypt-on-pa-1846585705", "https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/qvc2foo4ufow1cbs.jpg", "31-03-2021", "Whether youre looking to make a larger investment or you just want to dabble in cryptocurrencies, you can purchase Bitcoin, Ethereum, Bitcoin Cash, and Litecoin through PayPal.")


    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

if __name__ == '__main__':
    unittest.main()   