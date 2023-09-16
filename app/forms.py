from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    """
    This class represents the login web form
    It gets inputs from the user using wtforms fields.
    (StringField, PasswordField, SubmitField)
    """
    email = StringField('Email address', validators=[DataRequired(), Length(min=2, max=20), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    """
    This class represents the Sign up web form
    It gets inputs from the user using wtforms fields.
    (StringField, PasswordField, SubmitField)
    """
    email = StringField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
        
class CreateAccountForm(FlaskForm):
    """Create an account form"""
    firstname = StringField('First name', validators=[DataRequired()])
    lastname = StringField('Last name', validators=[DataRequired()])
    phonenumber = StringField('Phone number', validators=[DataRequired()])
    dob = DateField('Date of Birth:', validators=[DataRequired()], format='%m/%d/%Y')
    create = SubmitField('Create account')

    def validate_firstname(self, firstname):
        integer = 0
        try: 
            int(firstname)
            integer = 1
        except Exception:
            pass
        if integer == 1:
            ValidationError('Firstname must not be a number')
    
    def validate_lastname(self, lastname):
        integer = 0
        try: 
            int(lastname)
            integer = 1
        except Exception:
            pass
        if integer == 1:
            raise ValidationError('Lastname must not be a number')

    def validate_phonenumbe(self, phonenumber):
        """validate the phonenmber"""
        if phonenumber[0] == 0:
            phone_no = phonenumber[1:]
        try:
            int(phone_no)
        except Exception:
            raise ValidationError('Phonenumber cannot be words')