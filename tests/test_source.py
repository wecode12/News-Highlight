import unittest
from app.models import Source,Article
# Source = source.Source
# Article = article.Article

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("crypto-coins-news","Crypto Coins News","Providing breaking cryptocurrency news.", "https://www.ccn.com","technology","en","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
    def test_init(self):
        self.assertEqual(self.new_source.id,"crypto-coins-news")
        self.assertEqual(self.new_source.name,"Crypto Coins News")
        self.assertEqual(self.new_source.description,"Providing breaking cryptocurrency news.")
        self.assertEqual(self.new_source.url,"https://www.ccn.com")
        self.assertEqual(self.new_source.category,"technology")
        self.assertEqual(self.new_source.language,"en")
        self.assertEqual(self.new_source.country,"us")




class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("macrumors","Macrumors.com","Joe Rossignol","Brighter MicroLED and MiniLED Displays","Apple representatives attended the Touch Taiwan convention","https://www.macrumors.com","https://cdn.macrumors.com/article-new/2017/09/iphone-x-display.jpg?retina","2018-08-30T13:13:34Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        self.assertEqual(self.new_article.id,"macrumors")
        self.assertEqual(self.new_article.name,"Macrumors.com")
        self.assertEqual(self.new_article.author,"Joe Rossignol")
        self.assertEqual(self.new_article.title,"Brighter MicroLED and MiniLED Displays")
        self.assertEqual(self.new_article.description,"Apple representatives attended the Touch Taiwan convention")
        self.assertEqual(self.new_article.url,"https://www.macrumors.com")
        self.assertEqual(self.new_article.image,"https://cdn.macrumors.com/article-new/2017/09/iphone-x-display.jpg?retina")
        self.assertEqual(self.new_article.date,"2018-08-30T13:13:34Z")






