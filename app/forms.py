from flask_wtf import FlaskForm
from wtforms import  StringField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired

class propertyform(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    bedroom = StringField('No. of Bedrooms', validators=[DataRequired()])
    bathroom = StringField('No. of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    proptype = SelectField('Property Type', choices=[("Apartment", "Apartment"), ("House","House")])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])