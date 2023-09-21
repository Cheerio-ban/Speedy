from flask import Flask, redirect, render_template, request, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.forms import *
from app import app, db
from app.models import *
from datetime import datetime
import random




@app.route('/', methods=['GET'])
def home():    
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated and current_user.has_acc == 1:
        customer: Customer = Customer.query.filter_by(user_id=current_user.id).first()
        if customer.address.first() == None:
            return redirect(url_for('add_address', username=customer.username))
        return redirect(url_for('user_home', username=customer.username))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        if current_user.has_acc == 0:
            return redirect(url_for('create_account'))
        customer: Customer = Customer.query.filter_by(user_id=current_user.id).first()
        if customer.address.first() == None:
            return redirect(url_for('add_address', username=customer.username))
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('user_home', username=customer.username)
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated and current_user.has_acc == 1:
        customer: Customer = Customer.query.filter_by(user_id=current_user.id).first()
        if customer.address.first() == None:
            return redirect(url_for('add_address', username=customer.username))
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/create_account', methods=['GET', 'POST'])
@login_required
def create_account():
    if current_user.has_acc == 1:
        customer: Customer = Customer.query.filter_by(user_id=current_user.id).first()
        if customer.address.first() == None:
            return redirect(url_for('add_address', username=customer.username))
        return redirect('home')
    form = CreateAccountForm()
    if form.validate_on_submit():
        flash('Account successfully created')
        current_user.has_acc = 1
        customer =Customer()
        account = Account()
        account.create_account(form.data.pin)
        account.customer = customer
        customer.create_customer(form, account)
        customer.email = current_user.email
        customer.user_id = current_user.id
        account.cus_id = customer.id
        db.session.add(customer)
        db.session.commit()
        db.session.add(account)
        db.session.commit()
        return redirect(url_for('add_address', username=customer.username))
    return render_template('acc_creation.html', form=form)

@app.route('/<username>/add_address', methods=['GET', 'POST'])
@login_required
def add_address(username):
    customer: Customer = Customer.query.filter_by(user_id=current_user.id).first()
    if username != customer.username:
        return redirect(url_for('user_home', username=customer.username))
    form = FillAddress()
    if form.validate_on_submit():
        flash('Address Successfully added')
        customer = Customer.query.filter_by(user_id=current_user.id).first()
        address: Address = Address()
        address.cus_id = customer.id
        address.create_address(form)
        db.session.add(address)
        db.session.commit()
        return redirect(url_for('user_home', username=username))
    return render_template('set_address.html', form=form)

@app.route('/<username>/home')
@login_required
def user_home(username):
    customer: Customer = Customer.query.filter_by(user_id=current_user.id).first()
    account = Account.query.filter_by(cus_id=customer.id).first()
    if username != customer.username:
        return redirect(url_for('user_home', username=customer.username))
    return render_template('user_home.html', username=username, customer=customer, account=account)

@app.route('/<username>/profile', methods=['GET'])
@login_required
def profile(username):
    """Profile page for user"""
    customer: Customer = Customer.query.filter_by(user_id=current_user.id).first()
    accounts=Account.query.filter_by(cus_id=customer.id)
    if username != customer.username:
        return redirect(url_for('user_home', username=customer.username))
    return render_template('user_profile.html', username=customer.username, customer=customer)

@app.route('/<username>/profile/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile(username):
    """Edit the profile of the user"""
    customer: Customer = Customer.query.filter_by(user_id=current_user.id).first()
    if username != customer.username:
        return redirect(url_for('user_home', username=customer.username))
    form = EditProfileInfo()
    form2=EditProfileAddress()
    if form.validate_on_submit():
        customer.phone_number = form.phonenumber.data
        customer.username = form.username.data
        db.session.commit()
        return redirect(url_for('edit_profile', username=customer.username))
    if form2.validate_on_submit():
        address = Address.query.filter_by(cus_id=customer.id).first()
        address.create_address(form2)
        db.session.commit()
        return redirect(url_for('edit_profile', username=customer.username))
    return render_template('edit_profile.html', username=customer.username, customer=customer, form=form, form2=form2)


# @app.route('/<username>/profile', methods=['GET', 'POST'])
# def profile(username):
#     cus = Customer.query.filter_by(username=username).first()
#     account = cus.accounts.first()
#     address = cus.address.first()
#     return render_template('profile.html', customer=cus, account=account, address=address)

@app.route('/<username>/transactions')
def transactions(username):
    customer: Customer = Customer.query.filter_by(user_id=current_user.id).first()
    if username != customer.username:
        return redirect(url_for('user_home', username=customer.username))
    cus = Customer.query.filter_by(username=username).first()
    account = cus.accounts.first()
    transactions = account.transactions
    return render_template('transactions.html', transactions=transactions, account=account, customer=customer)


@app.route('/<username>/transfer', methods=['GET', 'POST'])
def transfer(username):
    customer = Customer.query.filter_by(user_id=current_user.id).first()
    user = User.query.all()
    form = Transfer()
    accounts = customer.accounts.all()
    if 'id' not in request.args:
        return redirect(url_for('transfer', id=accounts[0].id, username=customer.username))
    if form.validate_on_submit():
        transaction  = Transaction()
        id = request.args.get('id')
        account = Account.query.filter_by(id=request.args.get('id')).first()
        transaction.create_transaction(account, form)
        db.session.add(transaction)
        db.session.commit()
        return redirect(url_for('transactions', username=customer.username, id=id))
    return render_template('make_transfer.html', username=customer.username, form=form, customer=customer, users=user, accounts=accounts)

@app.route('/<username>/accounts')
def accounts(username):
    customer = Customer.query.filter_by(user_id=current_user.id).first()
    accounts = customer.accounts
    return render_template('accounts.html', customer=customer, accounts=accounts)

@app.route('/<username>/services')
def services(username):
    customer = Customer.get('user_id', current_user.id)
    return render_template('services.html', customer=customer)


@app.route('/footer')
def footer():
    return render_template('footer.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))