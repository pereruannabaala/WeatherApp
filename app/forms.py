from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask import request


class SearchForm(FlaskForm):
    q = StringField(
        'Search',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Search for a city'})

    def __init__(self, *args, **kwargs):
        # formdata is where Flask gets form submissions
        if 'formdata' not in kwargs:
            # GET request: request.args, POST: request.form
            kwargs['formdata'] = request.args
        if 'meta' not in kwargs:
            # Disable CSRF for clickable link
            kwargs['meta'] = {'csrf': False}
        super(SearchForm, self).__init__(*args, **kwargs)
