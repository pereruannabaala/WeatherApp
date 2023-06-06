# Sample Weather App

![Weather app](/app/static/images/weatherapp.gif)

### Table Of Contents

- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Test The Application](#test-the-application)
- [Using Weathermap API](#using-weathermap-api)


## How It Works

- Search for a city in the search bar
- Results automatically displayed on the web page in tabular form

## Technologies Used

- Flask (framework)
- Weathermap API (data)
- Flask bootstrap (styling)
- Flask wtf (forms)

## Test The Application

Live link: [weather map on Render](https://weather-map-fix.onrender.com)

### Locally

- Clone the repo:

    ```python
    $ git clone git@github.com:GitauHarrison/WeatherApp.git
    ```

- Change directory into the cloned repo:

    ```python
    $ cd WeatherApp
    ```

- Create and activate virtual environment:

    ```python
    # Normal way
    $ python -m venv venv
    $ source venv/bin/activate

    # OR using virtualenvwrapper
    $ mkvirtualenv venv
    ```

- Install project dependencies:

    ```python
    (venv)$ pip3 install -r requirements.txt
    ```

- Update configurations as seen in the `.env-template` file:

    ```python
    (venv)$ cp .env-template .env
    # Add values to these variables
    ```
    - A random SECRET_KEY value can be found by running the following in your terminal:
        ```python
        (venv)$ python3 -c 'import secrets; print(secrets.token_hex(16))'
        ```

- Run project:

    ```python
    (venv)$ flask run
    ```

- Paste http://localhost:5000 link into your browser's address bar. You should see the project
- Try search for a city


## Using Weathermap API

- Sign up for a free account [here](https://openweathermap.org/api).
- You will receive an email to verify your account. The email will contain your Weathermap API key. 
- Copy this API Key and store it in the `.env` file (it should not be pushed to version control; use `.gitignore`).
- The illustration used in this application is a forecast.
- A call to the API will return the following JSON:

    ```json
    {
    "coord": {
        "lon": 10.99,
        "lat": 44.34
    },
    "weather": [
        {
        "id": 501,
        "main": "Rain",
        "description": "moderate rain",
        "icon": "10d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 298.48,
        "feels_like": 298.74,
        "temp_min": 297.56,
        "temp_max": 300.05,
        "pressure": 1015,
        "humidity": 64,
        "sea_level": 1015,
        "grnd_level": 933
    },
    "visibility": 10000,
    "wind": {
        "speed": 0.62,
        "deg": 349,
        "gust": 1.18
    },
    "rain": {
        "1h": 3.16
    },
    "clouds": {
        "all": 100
    },
    "dt": 1661870592,
    "sys": {
        "type": 2,
        "id": 2075663,
        "country": "IT",
        "sunrise": 1661834187,
        "sunset": 1661882248
    },
    "timezone": 7200,
    "id": 3163858,
    "name": "Zocca",
    "cod": 200
    }                        
    ```

- Be guided by the keys seen above to access whatever data you want from your `city` (see `index.html`).
- More from the [documentation](https://openweathermap.org/current).