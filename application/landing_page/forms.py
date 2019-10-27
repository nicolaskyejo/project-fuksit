from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length


class SignupForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(message='Please enter a username.'),
                                       Length(min=3, max=30, message='Please enter at least 3 characters.')])
    password = PasswordField('Password',
                             validators=[DataRequired(message='Please enter a password.'),
                                         Length(min=6, max=100, message='Please enter at least six characters.')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(message='Please enter your username.')])
    password = PasswordField('Password',
                             validators=[DataRequired(message='Please enter your password.')])
    submit = SubmitField('Login')
