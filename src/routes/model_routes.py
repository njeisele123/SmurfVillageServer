import base64
import io

from flask import Blueprint, jsonify, send_file, make_response

from src.services.model_service import get_glb_bytes

glb_bp = Blueprint('glb', __name__)


# For sending GLB files to UI
# TODO: long-term these should be hosted in S3, but this keeps things simple for now

@glb_bp.route('/champion/<name>')
def summoner(name):
    print("name look up is: ", name)
    glb_bytes = get_glb_bytes(f'resources/glb/champions/{name}.glb')

    if glb_bytes is None:
        return jsonify({"error": "Internal Server Error"}), 500

    return make_response(glb_bytes)

