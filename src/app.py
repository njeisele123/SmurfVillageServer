import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import Index

from src.routes.model_routes import glb_bp
from src.routes.riot_routes import riot_bp

app = Flask(__name__)
CORS(app)  # enable CORS for all routes

# Configure SQLite database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)


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


# Create the database tables
with app.app_context():
    db.create_all()

# Routes
app.register_blueprint(riot_bp, url_prefix='/api/riot')
app.register_blueprint(glb_bp, url_prefix='/api/glb')

if __name__ == '__main__':
    app.run(debug=True)
