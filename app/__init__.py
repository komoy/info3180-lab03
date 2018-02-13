from flask_mail import Mail

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'party hard'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = 'e3cff7d539cd09'
app.config['MAIL_PASSWORD'] = '	d3e7e261e25d10'
mail = Mail(app)
from app import views