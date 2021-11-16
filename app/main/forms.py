
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField,FloatField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    submit = SubmitField('Save')

class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[Required()])
    short_description = StringField('Product Description', validators=[Required()])
    long_description = StringField('Product Description', validators=[Required()])
    price = FloatField('Enter the Product Prices', validators=[Required()])
    color = StringField("Enter Product Color", validators=[Required()])
    stock = StringField("Product Stock", validators=[Required()])
    brand = StringField("Brand", validators=[Required()])
    model = StringField("Product Model", validators=[Required()])
    category = StringField("Product Category", validators=[Required()])


    submit = SubmitField('Submit')