from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(), index=True, unique=True)
  password_hash = db.Column(db.String(128))

  def __repr__(self):
    return '<User {}>'.format(self.username)


class Customer(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(140))
  last_name = db.Column(db.String(140))
  email = db.Column(db.String(120), index=True, unique=True)
  phone_number = db.Column(db.Integer, primary_key=True)
  address = db.Column(db.String()) #Consider the feasibility of making this a table of its own.
  dob = db.Column(db.DateTime)
  date_created= db.Column(db.DateTime)
  accounts = db.relationship('Account', backref='customer', lazy='dynamic')


class Account(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  cus_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
  acc_type = db.Column(db.String)
  balance = db.Column(db.Integer)
  date_created = db.Column(db.DateTime)
  transactions = db.relationship('transaction', backref='account', lazy='dynamic')


class Transaction(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  acc_id = db.Column(db.Integer, db.ForeignKey('account.id'))
  transaction_type = db.Column(db.String)
  amount = db.Column(db.Integer)
  timestamp = db.Column(db.DateTime)