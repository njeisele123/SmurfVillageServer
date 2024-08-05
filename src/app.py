import os

from flask import Flask
from flask_cors import CORS

from src.models.models import db
from src.routes.model_routes import glb_bp
from src.routes.riot_routes import riot_bp
from src.routes.summoner_routes import summoner_bp

app = Flask(__name__)
CORS(app)  # enable CORS for all routes


# Configure SQLite database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Routes
app.register_blueprint(riot_bp, url_prefix='/api/riot')
app.register_blueprint(glb_bp, url_prefix='/api/glb')
app.register_blueprint(summoner_bp, url_prefix='/api/summoner')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # This creates the tables
    app.run(debug=True)
