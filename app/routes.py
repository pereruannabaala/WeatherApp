from app import app
from flask import render_template, url_for, redirect, g, session
from app.forms import SearchForm

# Executed before the a function
@app.before_request
def before_request():
    g.search_form = SearchForm()

# Define a vview function that renders the home page
# It will have a form to accept user input (city name)
# It will process the data needed to show the weather of the city
# Data will be passed to the templates for display
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    return render_template('index.html', title='Weather Data', form=form)
