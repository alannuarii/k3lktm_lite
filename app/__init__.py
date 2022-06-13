from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.models import user, lb3, debit_domestik, ph_domestik, debit_proses, ph_proses, sludge, oli_bekas, filter_bekas, majun_bekas, guestbook
from app import routes