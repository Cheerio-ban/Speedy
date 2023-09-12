from flask import Flask, render_template, url_for
from app.forms import LoginForm, RegistrationForm
from app import app


@app.route('/', methods=['GET'])
def landing():
    return render_template('landing.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('registration.html', form=form)