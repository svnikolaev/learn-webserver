from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from webapp.user.models import User


class LoginForm(FlaskForm):
    username = StringField(
        'Имя пользователя',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    password = PasswordField(
        'Пароль',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    remember_me = BooleanField(
        'Запомнить меня',
        default=True,
        render_kw={"class": "form-check-input"}
    )
    submit = SubmitField(
        'Войти',
        render_kw={"class": "btn btn-primary"}
    )


class RegistrationForm(FlaskForm):
    username = StringField(
        'Имя пользователя',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    email = StringField(
        'Электронная почта',
        validators=[DataRequired(), Email()],
        render_kw={"class": "form-control"}
    )
    password = PasswordField(
        'Пароль',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    repassword = PasswordField(
        'Повторите пароль',
        validators=[DataRequired(), EqualTo('password')],
        render_kw={"class": "form-control"}
    )
    submit = SubmitField(
        'Зарегистрироваться',
        render_kw={"class": "btn btn-primary"}
    )

    def validate_username(self, username):
        user_count = User.query.filter_by(username=username.data).count()
        print(user_count)
        print(bool(user_count))
        if user_count > 0:
            raise ValidationError(
                'Пользователь с таким именем уже зарегистрирован')

    def validate_email(self, email):
        email_count = User.query.filter_by(email=email.data).count()
        print(email_count)
        print(bool(email_count))
        if email_count > 0:
            raise ValidationError('Такая почта уже используется')
