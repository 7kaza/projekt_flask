from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Haslo', validators=[DataRequired()])
    remember_me = BooleanField('Zapamientaj mnie')
    submit = SubmitField('Zapisz sie')

class RegistrationForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Haslo', validators=[DataRequired()])
    password2 = PasswordField(
        'Powtorz haslo', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Prosze uzyj innego loginu.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Prosze uzyj innego adresu e-mail.')
