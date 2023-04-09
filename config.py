
from flask_sqlalchemy import SQLAlchemy
db_map = {
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///database.db',
    'SECRET_KEY': 'thisisasecretkey'
}


db = SQLAlchemy()
