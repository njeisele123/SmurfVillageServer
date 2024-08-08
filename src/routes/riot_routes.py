from flask import Blueprint, jsonify
from src.services.riot_service import get_summoner_data, get_matches, get_match, get_summoner_by_id, get_league_entries

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


@riot_bp.route('/summoner-by-id/<puuid>')
def summoner_by_id(puuid):
    data = get_summoner_by_id(puuid)
    print("by-name ", data)
    return jsonify(data)


@riot_bp.route('/league-entries/<summoner_id>')
def league_entries(summoner_id):
    data = get_league_entries(summoner_id)
    return jsonify(data)
