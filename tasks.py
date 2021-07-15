from celery import Celery
from webapp import create_app
from webapp.news.parsers import habr
# from webapp.python_org_news import get_python_news

flask_app = create_app()
celery_app = Celery('tasks', broker='redis://192.168.1.72:6379/0')


@celery_app.task
def habr_snippets():
    with flask_app.app_context():
        habr.get_news_snippets()


@celery_app.task
def habr_content():
    with flask_app.app_context():
        habr.get_news_content()
