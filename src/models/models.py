from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Index


# Initialize SQLAlchemy
db = SQLAlchemy()


# Data model
class Summoner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(30), unique=False, nullable=False)
    summoner_name = db.Column(db.String(30), nullable=False)
    tag_line = db.Column(db.String(10), nullable=False)

    # Add an index to the 'ip' column
    __table_args__ = (Index('idx_summoner_ip', 'ip'),)

    def __repr__(self):
        return f'<Summoner {self.summoner_name}>'



