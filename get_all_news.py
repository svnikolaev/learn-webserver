from webapp import create_app
from webapp.news.parsers import habr
# from webapp.python_org_news import get_python_news

app = create_app()
with app.app_context():
    habr.get_news_snippets()
    habr.get_news_content()
