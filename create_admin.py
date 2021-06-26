from getpass import getpass
import sys

from webapp import create_app
from webapp.model import db, User

app = create_app()

with app.app_context():
    username = input("Введите имя пользователя: ")

    if User.query.filter(User.username == username).count():
        print("Пользователь с таким именем уже существует")
        sys.exit(0)

    password = getpass('Введите пароль: ')
    password_repeated = getpass('Повторите пароль: ')

    if not password == password_repeated:
        print("Пароли не одинаковые")
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print('Пользователь с id {} создан'.format(new_user.id))
