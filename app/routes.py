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
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        if current_user.has_acc == 0:
            return render_template('no_acc.html', form=form)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
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
        return redirect('home')
    form = CreateAccountForm()
    if form.validate_on_submit():
        account = Account()
        account.date_created = datetime.strftime(datetime.utcnow(), "%m/%d/%Y")
        account.cus_id = current_user.id
        account.create_account_number()
        account.acc_type
    return render_template('create_account.html', form=form)

@app.route('/transactions')
def transactions():
    return render_template('transactions.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))