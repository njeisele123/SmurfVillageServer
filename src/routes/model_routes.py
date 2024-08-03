import base64

from flask import Blueprint, jsonify

from src.services.model_service import get_glb_bytes

glb_bp = Blueprint('glb', __name__)


# For sending GLB files to UI

@glb_bp.route('/champion/<name>')
def summoner(name):
    glb_bytes = get_glb_bytes(f'resources/glb/champions/{name}.glb')
    if glb_bytes is None:
        return jsonify({"error": "Internal Server Error"}), 500

    encoded_bytes = base64.b64encode(glb_bytes).decode('utf-8')
    return jsonify({"bytes": encoded_bytes}), 200
