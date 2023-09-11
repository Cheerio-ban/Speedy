from flask import Flask, render_template
from app import app


@app.route('/', methods=['GET'])
def landing():
    return render_template('landing.html')