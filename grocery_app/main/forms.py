from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from grocery_app.extensions import bcrypt
from wtforms.validators import DataRequired, Length
from grocery_app.models import *

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    title = StringField('Store Name', 
        validators=[
            DataRequired(),
            Length(min=3, max=80, message="Your store must be between 3 and 80 characters.")
        ])
    address = StringField('Location', 
        validators=[
            DataRequired(),
            Length(min=3, max=80, message="Your address must be between 3 and 80 characters.")
        ])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    name = StringField('Item name', validators=[
        DataRequired(),
        Length(min=3, max=80, message="Item must be between 3 and 80 characters.")
    ])
    price = FloatField('Item price', validators=[DataRequired()])
    category = SelectField('Category', choices=ItemCategory.choices())
    photo_url = StringField('Url', validators=[DataRequired()])
    store = QuerySelectField('Store', 
        query_factory=lambda: GroceryStore.query, allow_blank=False)
    submit = SubmitField('Submit')
