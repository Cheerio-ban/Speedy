from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(), index=True, unique=True)
  password_hash = db.Column(db.String(128))


  def __repr__(self):
    return '<User {}>'.format(self.username)


class Customer(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
  first_name = db.Column(db.String(140))
  last_name = db.Column(db.String(140))
  email = db.Column(db.String(120), index=True, unique=True)
  phone_number = db.Column(db.String(204), primary_key=True)
  address = db.relationship('Address', backref='customer', lazy='dynamic')
  dob = db.Column(db.DateTime)
  date_created= db.Column(db.DateTime)
  bank_name = db.Column(db.String(240), default="Speedy")
  accounts = db.relationship('Account', backref='customer', lazy='dynamic')


class Account(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  cus_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
  account_number = db.Column(db.String(100), nullable=False)
  account_pin = db.Column(db.String(4), default='0022')
  acc_type = db.Column(db.String(240))
  balance = db.Column(db.Integer)
  bank_name = db.Column(db.String(240), default="Speedy", nullable=False)
  date_created = db.Column(db.DateTime)
  transactions = db.relationship('Transaction', backref='account', lazy='dynamic')


class Transaction(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  acc_num = db.Column(db.String(100), db.ForeignKey('account.account_number'))
  bank_name = db.Column(db.String(240), default="Speedy", nullable=False)
  transaction_type = db.Column(db.String(240))
  amount = db.Column(db.Integer)
  timestamp = db.Column(db.DateTime)

class Address(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  cus_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
  apartment_number = db.Column(db.Integer, nullable=False)
  street_number = db.Column(db.Integer, nullable=False)
  street_name = db.Column(db.String(256), nullable=False)
  city = db.Column(db.String(256), nullable=False)
  state = db.Column(db.String(256), nullable=False)
  country = db.Column(db.String(256), nullable=False)
  postal_code = db.Column(db.Integer)
  address_line_2 = db.Column(db.String(400))
