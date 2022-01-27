from apps.models import Model


class News(Model):
    __table__ = 'news'
    __primary_key__ = 'id'