from flask import Blueprint, jsonify
from src.services.riot_service import get_summoner_data, get_matches, get_match

riot_bp = Blueprint('riot', __name__)


@riot_bp.route('/summoner/<summoner_name>/<tag_line>')
def summoner(summoner_name, tag_line):
    data = get_summoner_data(summoner_name, tag_line)
    return jsonify(data)


@riot_bp.route('/matches/<puuid>')
def matches(puuid):
    data = get_matches(puuid)
    return jsonify(data)


@riot_bp.route('/match/<mid>')
def match(mid):
    data = get_match(mid)
    return jsonify(data)
