from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    q = StringField(
        'Search',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Search for a city'})
