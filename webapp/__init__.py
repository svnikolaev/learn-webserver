from threading import current_thread
from flask import Flask, flash, render_template, redirect, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
# from requests.models import guess_json_utf
from webapp.forms import LoginForm
from webapp.model import db, News, User
from webapp.weather import weather_by_city
# from webapp.python_org_news import get_python_news


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        print("Отладка index")
        print(current_user)
        title = "Новости Python"
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        # news_list = get_python_news()
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template('index.html',
                               title=title,
                               weather=weather,
                               news_list=news_list)

    @app.route('/login')
    def login():
        print("Отладка login")
        print(current_user.is_authenticated)
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', title=title, form=login_form)

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()

        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash("Вы успешно вошли на сайт")
                return redirect(url_for('index'))
        flash('Неправильные имя или пароль')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return "Привет, админ!"
        else:
            return "Ты не админ!"

    return app

# if __name__ == "__main__":
#     app.run(debug=True)
