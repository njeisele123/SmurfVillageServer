from flask import Blueprint, jsonify

from src.app import Summoner
from src.services.riot_service import get_summoner_data, get_matches, get_match

summoner_bp = Blueprint('summoner', __name__)


@summoner_bp.route('/summoner/<int:ip_address>', methods=['GET'])
def get_summoner(ip_address):
    # TODO: try/catch
    summoners = Summoner.query.filter_by(ip=ip_address).all()
    return jsonify([
        {
            'id': s.id,
            'ip': s.ip,
            'summoner_name': s.summoner_name,
            'tag_line': s.tag_line
        } for s in summoners
    ])
