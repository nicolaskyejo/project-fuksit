from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, SelectMultipleField, widgets
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length
from random import randrange


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


#  https://github.com/mjhea0/thinkful-mentor/tree/master/python/flask-wtf-quiz
class CorrectAnswer(object):
    """
    Custom validator for WTForms to check
    if the correct answer was submitted
    """

    def __init__(self, answer):
        self.answer = answer

    def __call__(self, form, field):
        # List of error messages that are selected by random
        error_messages = ['Sorry, that\'s not the correct answer.',
                          'Try that again...',
                          'Incorrect answer.',
                          'Please check this answer...',
                          'Oops! Try again...',
                          'Nope! Sorry... try again!',
                          'No, not quite... try again!',
                          'Hmmm, not exactly right...']
        num = randrange(0, len(error_messages))
        message = error_messages[num]

        if field.data != self.answer:
            raise ValidationError(message)


class Quiz(FlaskForm):
    q1 = RadioField(
        "1. How many campuses are there?",
        choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'),('4', 'Four'), ('5', 'Five')],
        validators=[CorrectAnswer('4')]
        )

    q2 = RadioField(
        "2. Before OMA, what was the name of the school intranet?",
        choices=[('MyNet', 'MyNet'), ('Tuubi', 'Tuubi'), ('MetroNet', 'MetroNet'), ('SchoolNet', 'SchoolNet')],
        validators=[CorrectAnswer('Tuubi')]
        )

    q3 = RadioField(
        "3. What does METKA stand for?",
        choices=[('Metropolia AMK student union', 'Metropolia Ammattikorkeakoulun opiskelijakunta'),
                 ('Metropolia Eettinen', 'Metropolia eettinen'), ('Metropolia Etu', 'Metropolia Etu')],
        validators=[CorrectAnswer('Metropolia AMK student union')]
    )
    # q4 = RadioField(
    #     "4. What year was Metropolia University of Applied Sciences founded?",
    #     choices=[('', ''), ('', ''), ('', ''), ('', '')],
    #     validators=[CorrectAnswer('')]
    # )
    # q5 = RadioField(
    #     "5. Roughly how many teachers  are there in Metropolia?",
    #     choices=[('', ''), ('', ''), ('', ''), ('', '')],
    #     validators=[CorrectAnswer('')]
    # )
    # q6 = RadioField(
    #     "6. Approximately how many students study in Metropolia?",
    #     choices=[('', ''), ('', ''), ('', ''), ('', '')],
    #     validators=[CorrectAnswer('')]
    # )
    # q7 = RadioField(
    #     "7. Who is the current head of the school?",
    #     choices=[('', ''), ('', ''), ('', ''), ('', '')],
    #     validators=[CorrectAnswer('')]
    # )
    # q8 = RadioField(
    #     "8. Who owns Metropolia?",
    #     choices=[('', ''), ('', ''), ('', ''), ('', '')],
    #     validators=[CorrectAnswer('')]
    # )
    # q9 = RadioField(
    #     "9. What does OMA stand for?",
    #     choices=[('', ''), ('', ''), ('', ''), ('', '')],
    #     validators=[CorrectAnswer('')]
    # )
    # q10 = RadioField(
    #     "10. How many degree programs are offered in Metropolia?",
    #     choices=[('', ''), ('', ''), ('', ''), ('', '')],
    #     validators=[CorrectAnswer('')]
    # )
    q11 = RadioField(
        "11. Which universities constitute the 3UAS partnership?",
        choices=[('Haaga-Helia, Laurea and Metropolia', 'Haaga-Helia, Laurea and Metropolia'),
                 ('Haaga-Helia, Aalto and Metropolia', 'Haaga-Helia, Aalto and Metropolia'),
                 ('Amiedu, Omnia and Metropolia', 'Amiedu, Omnia and Metropolia'),
                 ('Aalto, University of Helsinki, and Metropolia', 'Aalto, University of Helsinki, and Metropolia')],
        validators=[CorrectAnswer('Haaga-Helia, Laurea and Metropolia')]
    )

    submit = SubmitField("Submit")
