from flask import Flask, jsonify
from flask_cors import CORS

from src.routes.model_routes import glb_bp
from src.routes.riot_routes import riot_bp

app = Flask(__name__)
CORS(app)  # enable CORS for all routes

app.register_blueprint(riot_bp, url_prefix='/api/riot')
app.register_blueprint(glb_bp, url_prefix='/api/glb')

if __name__ == '__main__':
    app.run(debug=True)