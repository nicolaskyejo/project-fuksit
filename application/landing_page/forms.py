from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length
from random import randrange


class SignupForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(message='Please enter a username.'),
                                       Length(min=3, max=30, message='Please enter a username between 3-30 characters.')])
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
        "1. How many campuses are there currently?",
        choices=[('7', 'Seven'), ('4', 'Four'), ('5', 'Five'), ('8', 'Eight')],
        validators=[CorrectAnswer('8')]
        )

    q2 = RadioField(
        "2. Before OMA, what was the name of the school intranet?",
        choices=[('MyNet', 'MyNet'), ('Tuubi', 'Tuubi'), ('MetroNet', 'MetroNet'), ('SchoolNet', 'SchoolNet')],
        validators=[CorrectAnswer('Tuubi')]
        )

    q3 = RadioField(
        "3. What does the acronym METKA stand for?",
        choices=[('Metropolia AMK student union', 'Metropolia Ammattikorkeakoulun opiskelijakunta'),
                 ('Metropolian eliitti', 'Metropolian eliitti-tutkinnon kunniakkaat alisuorittajat'),
                 ('Metropolian metkat menninkäiset', 'Metropolian metkat menninkäiset'),
                 ('Metropolian työttömät karavaanarit', 'Metropolian työttömät karavaanarit')],
        validators=[CorrectAnswer('Metropolia AMK student union')]
    )
    q4 = RadioField(
        "4. What year was Metropolia University of Applied Sciences founded?",
        choices=[('2011', '2011'), ('2014', '2014'), ('2007', '2007'), ('2009', '2009')],
        validators=[CorrectAnswer('2007')]
    )
    q5 = RadioField(
        "5. Roughly how many teachers  are there in Metropolia?",
        choices=[('250', '250'), ('600', '600'), ('460', '460'), ('570', '570')],
        validators=[CorrectAnswer('570')]
    )
    q6 = RadioField(
        "6. Approximately how many students study in Metropolia?",
        choices=[('1111', '1111'), ('16400', '16400'), ('9000', '9000'), ('12500', '12500')],
        validators=[CorrectAnswer('16400')]
    )
    q7 = RadioField(
        "7. Who is the current head of the school (CEO)?",
        choices=[('Timo Salin', 'Timo Salin'), ('Janne Salonen', 'Janne Salonen'),
                 ('Päivi Haapasalmi', 'Päivi Haapasalmi'), ('Riitta Konkola', 'Riitta Konkola')],
        validators=[CorrectAnswer('Riitta Konkola')]
    )

    q8 = RadioField(
        "8. What does OMA stand for?",
        choices=[('Online Metropolia Account', 'Online Metropolia Account'),
                 ('Nothing', 'Does not stand for anything'),
                 ('Oikein Mainio Avustin', 'Oikein Mainio Avustin'),
                 ('Oppilaiden Materiaali Arkisto', 'Oppilaiden Materiaali Arkisto')],
        validators=[CorrectAnswer('Nothing')]
    )
    q9 = RadioField(
        "9. How many degree programs are offered in Metropolia?",
        choices=[('55', '55'), ('69', '69'), ('60', '60'), ('80', '80')],
        validators=[CorrectAnswer('69')]
    )
    q10 = RadioField(
        "10. Which universities constitute the 3UAS partnership?",
        choices=[('Haaga-Helia, Laurea and Metropolia', 'Haaga-Helia, Laurea and Metropolia'),
                 ('Haaga-Helia, Aalto and Metropolia', 'Haaga-Helia, Aalto and Metropolia'),
                 ('Amiedu, Omnia and Metropolia', 'Amiedu, Omnia and Metropolia'),
                 ('Aalto, University of Helsinki, and Metropolia', 'Aalto, University of Helsinki, and Metropolia')],
        validators=[CorrectAnswer('Haaga-Helia, Laurea and Metropolia')]
    )

    submit = SubmitField("Submit")
