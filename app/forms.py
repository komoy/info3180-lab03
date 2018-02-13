from flask_wtf import FlaskForm

from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 

from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField('name',validators=[DataRequired()])
    email = StringField('email',validators=[DataRequired()])
    subject = StringField('subject',validators=[DataRequired()])
    message = TextAreaField('message',validators=[DataRequired()])
    