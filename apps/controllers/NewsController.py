from apps.validation.NewsValidator import validate_link
from apps.services.NewsServices.NewsScraper import NewsScraper
from apps.services.NewsServices.NewsPostgres import NewsPostgres


class NewsController(object):
    def __init__(self) -> None:
        pass
    
    @classmethod
    def scrape_news(self):
        data = NewsScraper.get_news()
        return len(data), data

    @classmethod
    def get_news(self):
        data = NewsPostgres.get_news()
        return len(data), data

    @classmethod
    def get_news_by_word(self, word: str):
        data = NewsPostgres.get_news_by_word(word)
        return len(data), data

    @classmethod
    def get_news_by_title(self, title: str):
        data = NewsPostgres.get_news_by_title(title)
        return data

    @classmethod
    def get_news_by_link(self, link: str):
        data = NewsPostgres.get_news_by_link(link)

        if not data:
            val, msg = validate_link(link)
            
            if not val:
                return data, msg

            data = NewsScraper.get_newspage(link)
            return data, msg

        return data, 'url found in database'

