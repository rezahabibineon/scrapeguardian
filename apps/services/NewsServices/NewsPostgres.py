from apps.helper import Log
from orator.exceptions.orm import ModelNotFound
from apps.models import db
from apps.models.NewsModel import News


class NewsPostgres:

    @classmethod
    def check_news(cls, input):
        try:
            news = News.where('link', '=', input).first_or_fail().serialize()
            return news

        except ModelNotFound as e:
            Log.info(e)
            return {}

    @classmethod
    def save_news(cls, input):
        try:
            news = News.where('title', '=', input['title']).first_or_fail().serialize()
            return news

        except ModelNotFound as e:
            Log.info(e)
            db.table('news').insert(input)

    @classmethod
    def get_news(cls):
        try:
            news = News.all().serialize()
            return news
        except Exception as e:
            Log.info(e)
            return []

    @classmethod
    def get_news_by_word(cls, word):
        try:
            word = word.title()
            news = News.where('title', 'like', f'%{word}%').get().serialize()
            return news
        except ModelNotFound as e:
            Log.info(e)
            return []

    @classmethod
    def get_news_by_title(cls, title):
        try:
            news = News.where('title', '=', title).first_or_fail().serialize()
            return news

        except ModelNotFound as e:
            Log.info(e)
            return {}

    @classmethod
    def get_news_by_link(cls, link):
        try:
            news = News.where('link', '=', link).first_or_fail().serialize()
            return news

        except ModelNotFound as e:
            Log.info(e)
            return {}       
