from app import app
from flask import render_template, url_for, redirect


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def home():
    return render_template('index.html', title='Home')
