from flask import Flask, render_template
# from requests.models import guess_json_utf
from webapp.model import db, News
from webapp.weather import weather_by_city
# from webapp.python_org_news import get_python_news

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title = "Новости Python"
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        # news_list = get_python_news()
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', title=title, weather=weather, news_list=news_list)

    return app

# if __name__ == "__main__":
#     app.run(debug=True)