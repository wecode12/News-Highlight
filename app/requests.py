
import urllib.request
import json
# from .models import Source
from .models import Source,Article

# Source = source.Source
# Article = article.Article

# Getting api key
api_key = None
# api_key='3f7ad7ad6ae546a28feead545feea3c4'

# Getting the sources base url
base_url = None
# Getting the article url
articles_url = None
# to headlines
headlines_url = None

def configure_request(app):
    global api_key,base_url,articles_url,headlines_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config["NEWS_API_BASE_URL"]
    articles_url = app.config["ARTICLES_URL"]
    headlines_url = app.config["HEADLINES_URL"]



# Getting the sources base url
# base_url = app.config["NEWS_API_BASE_URL"]
# Getting the article url
# articles_url = app.config["ARTICLES_URL"]
# to headlines
# headlines_url = app.config["HEADLINES_URL"]

def get_sources_by_cat(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)


    return source_results

def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain source details
    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if description:
            source_object = Source(id,name,description,url,category,language,country)
            source_results.append(source_object)
    

    return source_results

def get_all_articles(id):
    get_articles_url = articles_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_sources_response = json.loads(get_articles_data)

        article_results = None

        if get_sources_response['articles']:
            article_results_list = get_sources_response['articles']
            article_results = process_article_results(article_results_list)


    return article_results

def process_article_results(article_list):

    article_results = []
    for articles in article_list:
    
        id = articles.get('source.id')
        name = articles.get('source.name')
        author =articles.get('author')
        title = articles.get('title')
        description = articles.get('description')
        url = articles.get('url')
        image = articles.get('urlToImage')
        date= articles.get('publishedAt')

        if image and date:
            article_object = Article(id,name,author,title,description,url,image,date)
            article_results.append(article_object)

    return article_results

def get_headline_articles(language):
    get_articles_url = headlines_url.format(language,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_sources_response = json.loads(get_articles_data)

        article_results = None

        if get_sources_response['articles']:
            article_results_list = get_sources_response['articles']
            article_results = process_article_results(article_results_list)


    return article_results