from app import db
from flask_login import UserMixin
from app import login
from werkzeug.security import check_password_hash, generate_password_hash
import random
from datetime import datetime


class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(), index=True, nullable=False, unique=True)
  password_hash = db.Column(db.String(128))
  has_acc = db.Column(db.Integer, default=0, nullable=False)
  def __repr__(self):
    return '<User {}>'.format(self.email)
    
  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

  def associated(self):
    """This returns associated objects in the db"""
    id = self.id
    customer = Customer.query.filter_by(user_id=id).first()
    account = Account.query.filter_by(cus_id=customer.id).first()
    return [customer, account]

class Account(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  cus_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
  account_number = db.Column(db.String(100), nullable=False)
  account_pin = db.Column(db.String(4))
  acc_type = db.Column(db.String(240))
  balance = db.Column(db.Integer)
  bank_name = db.Column(db.String(240), default="Speedy", nullable=False)
  date_created = db.Column(db.DateTime, default=datetime.utcnow)
  transactions = db.relationship('Transaction', backref='account', lazy='dynamic')

  def create_account_number(self):
    """This function will use the random module to create a unique number"""
    exists = True #bool for if the generated account number exists
    #while exists:
    number = random.randint(111111111, 999999999)
    acc_no = Account.query.filter_by(account_number=number).first()
    if acc_no is None:
      exist = False
    self.account_number = number

  def create_account(self, pin):
    """This creates the accoi=unt based on the form's data"""
    self.date_created = datetime.utcnow()
    self.create_account_number()
    self.acc_type = 'active'
    self.balance = 0
    self.account_pin = generate_password_hash(str(pin))

  def check_pin(self, pin):
    """Chc=eck to see if a provided pin is correct"""
    return check_password_hash(self.account_pin, str(pin))

class Customer(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
  first_name = db.Column(db.String(140))
  last_name = db.Column(db.String(140))
  email = db.Column(db.String(120), index=True, unique=True)
  phone_number = db.Column(db.String(204), unique=True)
  username = db.Column(db.String(200))
  address = db.relationship('Address', backref='customer', lazy='dynamic')
  dob = db.Column(db.DateTime)
  date_created= db.Column(db.DateTime, default=datetime.utcnow)
  bank_name = db.Column(db.String(240), default="Speedy")
  accounts = db.relationship('Account', backref='customer', lazy='dynamic')

  def __repr__(self):
      return "Customer: {} {}".format(self.first_name, self.last_name)

  @classmethod
  def get(cls, param, arg):
    """Get a customer from the database based on information given"""
    if param == "id":
      customer = Customer.query.filter_by(id=arg).first()
    elif param == "user_id":
      customer = Customer.query.filter_by(user_id=arg).first()
    elif param == "email":
      customer = Customer.query.filter_by(email=arg).first()
    elif param == "phone_number":
      customer == Customer.query.filter_by(phone_number=arg).first()
    else:
      customer = None
    return customer
  
  def format_time(self, date: datetime):
    """This to format object to string"""
    format = ("%B %d %Y")
    return datetime.strftime(date, format)

  def get_address(self):
    """Get customer address"""
    return self.address.first()
  
  def get_accounts(self):
    """Get accounts from the customer"""
    return self.accounts.all()


  def create_customer(self, form, account: Account):
    """This function is to assign values to the attributes of the object"""
    self.first_name = form.firstname.data
    self.last_name = form.lastname.data
    self.dob = form.dob.data
    self.date_created = account.date_created
    self.phone_number = form.phonenumber.data
    self.username = form.username.data


class Transaction(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(250))
  acc_num = db.Column(db.String(100), db.ForeignKey('account.account_number'))
  bank_name = db.Column(db.String(240), default="Speedy", nullable=False)
  transaction_type = db.Column(db.String(240))
  amount = db.Column(db.Integer)
  timestamp = db.Column(db.DateTime)
  initial_balance = db.Column(db.Integer)
  balance = db.Column(db.Integer)

  def format_time(self, time):
    """Format time"""
    return datetime.strftime(time, '%m/%d/%Y')
  
  def create_transaction(self, account: Account, form):
    """This creates a transaction object and modifies the account accordingly"""
    self.description = form.description.data
    self.acc_num = account.account_number
    self.bank_name = form.bank_name.data
    self.amount = int(form.amount.data)
    self.transaction_type = 'Debit'
    self.initial_balance = account.balance
    self.balance = account.balance - int(self.amount)
    self.timestamp = datetime.utcnow()
    account.balance = account.balance - int(self.amount)




class Address(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  cus_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
  apartment_number = db.Column(db.Integer, nullable=False)
  street_number = db.Column(db.Integer)
  street_name = db.Column(db.String(256), nullable=False)
  city = db.Column(db.String(256), nullable=False)
  state = db.Column(db.String(256), nullable=False)
  country = db.Column(db.String(256), nullable=False)
  postal_code = db.Column(db.Integer)
  address_line_2 = db.Column(db.String(400))

  def create_address(self, form):
    """Fill in the address attribute """
    self.apartment_number = form.apartment_number.data
    self.street_name = form.street_name.data
    self.city = form.city.data
    self.state = form.state.data
    self.country = form.country.data
    self.postal_code = form.postal_code.data
    self.address_line_2 = form.address_line_2.data


@login.user_loader
def load_user(id):
  return User.query.get(int(id))