import requests

from webapp.db import db
from webapp.news.models import News


def get_html(url):
    headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0)'
                       ' Gecko/20100101 Firefox/89.0')
    }
    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        print(result)
        return result.text
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False


def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    print(news_exists)
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()
