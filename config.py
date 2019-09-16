

import os

class Config:
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    ARTICLES_URL ='https://newsapi.org/v2/everything?q={}&apiKey={}'
   
    HEADLINES_URL ='https://newsapi.org/v2/top-headlines?language={}&apiKey={}'
    NEWS_API_KEY ='f85b298aaced4c6793886941d5c0f899'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}
