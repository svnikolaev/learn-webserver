from flask import Blueprint, current_app, render_template

from webapp.news.models import News
from webapp.weather import weather_by_city

blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    title = "Новости Python"
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    # news_list = get_python_news()
    news_list = News.query.order_by(News.published.desc()).all()
    return render_template('news/index.html',
                           title=title,
                           weather=weather,
                           news_list=news_list)
