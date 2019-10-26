from wtforms import Form, StringField, PasswordField, validators, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, Optional


class SignupForm(Form):
    username = StringField('Username',
                           validators=[DataRequired(message='Please enter a username.'),
                                       Length(min=3, message='Please enter at least 3 characters.')])
    password = PasswordField('Password',
                             validators=[DataRequired(message='Please enter a password.'),
                                         Length(min=6, message='Please enter at least six characters.')])
    submit = SubmitField('Register')


class LoginForm(Form):
    username = StringField('Username',
                           validators=[DataRequired(message='Please enter your username.')])
    password = PasswordField('Password',
                             validators=[DataRequired(message='Please enter your password.')])
    submit = SubmitField('Log in')
