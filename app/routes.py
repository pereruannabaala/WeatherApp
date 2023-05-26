from app import app
from flask import render_template, url_for, redirect, g, request, \
    flash, Response, json, session
from app.forms import SearchForm
import urllib

# Executed before the a function
@app.before_request
def before_request():
    g.search_form = SearchForm()

# Define a vview function that renders the home page
# It will have a form to accept user input (city name)
# It will process the data needed to show the weather of the city
# Data will be passed to the templates for display
@app.route('/')
@app.route('/index')
def index():
    city = request.args.get('q')
    print('City:', city)
    if city is not None:
        data = {}
        data['q'] = city
        print(data['q'])
        data['appid'] = app.config['WEATHERMAP_API']
        data['units'] = 'metrics'
        url_values = urllib.parse.urlencode(data)
        url = 'http://api.openweathermap.org/data/2.5/forecast'
        full_url = url + '?' + url_values
        data = urllib.request.urlopen(full_url)
        resp = Response(data)
        print(resp.status_code)
        data=json.loads(data.read().decode('utf8'))
        print(data['list'])
    else:
        flash('No city given. Add a city using the search form to see weather details.')
        data = {}
    return render_template(
        'index.html',
        title=f'Weather Data For {city}',
        city=city,
        data=data)
