import os
from flask import Flask
import ConfigParser
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

config = ConfigParser.ConfigParser()
config.read(os.path.dirname(os.path.abspath(__file__)) + '/config.ini')

app = Flask(__name__)
app.config['SECRET_KEY'] = config.get('SERVER', 'SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
										config.get('SERVER', 'MYSQL_USER') + ':' + \
										config.get('SERVER', 'MYSQL_PASSWORD') + '@' + \
										config.get('SERVER', 'MYSQL_SERVER') + '/' + \
										config.get('SERVER', 'MYSQL_DATABASE')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/SampleSearchApp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)


from app import routes, models