from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, URLField, EmailField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, URL
import sqlalchemy as sa
from webapp.db import db
from webapp.models import User

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    email = EmailField('Электронная почта', validators=[DataRequired(), Email()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError('Пользователь с таким именем уже существует')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError('Пользователь с такой почтой уже существует')


class AddParsingForm(FlaskForm):
    url_to_the_category = URLField('Cсылка на категорию',
                    validators=[DataRequired(message="Введите ссылку на категорию"),
                    URL(message="Введите валидную ссылку на категорию")], 
                    render_kw={"class":"form-control"})
    notification_email = EmailField('Почта для уведомлений', 
                    validators=[DataRequired(message="Введите Email"), 
                    Email(message="Введите валидный Email")], 
                    render_kw={"class":"form-control"})
    polling_interval = IntegerField('Интервал опроса (сек.)', validators=[DataRequired()], 
                    render_kw={"class":"form-control"})
    submit = SubmitField('Отправить!', render_kw={"class":"btn btn-primary"})
