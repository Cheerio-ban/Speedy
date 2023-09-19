from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import Regexp, Length
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    """
    This class represents the login web form
    It gets inputs from the user using wtforms fields.
    (StringField, PasswordField, SubmitField)
    """
    email = StringField('Email address', validators=[DataRequired(), Length(min=7, max=40), Email()])
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
    username = StringField('Username', validators=[DataRequired()])
    phonenumber = StringField('Phone number', validators=[DataRequired()])
    dob = DateField('Date of Birth:', validators=[DataRequired()], format='%Y-%m-%d')
    pin = StringField('Set Pin', validators=[DataRequired(), Length(min=4, max=4, message="Pin must be 4 digits"), Regexp(regex=r'\d*', message='Values must be digits')])
    email = StringField('Email')
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

    def validate_phonenumber(self, phonenumber):
        """validate the phonenmber"""
        phone_no = phonenumber.data
        if phonenumber.data[0] == 0:
            phone_no = phonenumber.data[1:]
        try:
            int(phone_no)
        except Exception:
            raise ValidationError('Phonenumber cannot be words')
    
    def validate_pin(self, pin):
        try:
            int(pin.data)
        except Exception:
            raise ValidationError('The pin should be digits')   


class FillAddress(FlaskForm):
    """This is a class of form to fill address"""
    apartment_number = StringField('Apartment number', validators=[DataRequired(), Regexp(regex=r'\d*', message='Values must be digits')])
    street_name = StringField('Street name', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    postal_code = StringField('Postal Code', validators=[Regexp(regex=r'\d*', message='Values must be digits')])
    address_line_2 = StringField('Address Line 2')
    submit = SubmitField('Add address')


class InterTransfer(FlaskForm):
    """Form to carry out transfers"""
    amount = StringField('Amount')
    acc_number = StringField('Beneficiary Account Number', validators=[DataRequired()])
    bank_name = StringField('Beneficiary Bank Number', validators=[DataRequired()])
    from_acc = StringField('From Account')
    submit = SubmitField('Transfer')