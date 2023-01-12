import requests 
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG']=True
#configuration value for database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
  
db= SQLAlchemy(app)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50), null=False)




@app.route('/')
def index():
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&APPID=7ddd4e724294f24845adb063481c6d43'
    city='Las Vegas'

    r=requests.get(url.format(city)).json()
    

    weather={
        'city': city,
        'temperature':r['main']['temp'],
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon'],
    }

    print(weather)
    return render_template('index.html', weather=weather)