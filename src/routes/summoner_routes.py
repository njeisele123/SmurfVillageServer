from flask import Blueprint, jsonify, request

from src.models.models import Summoner, db

summoner_bp = Blueprint('summoner', __name__)


@summoner_bp.route('/accounts/<string:ip_address>', methods=['GET'])
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


@summoner_bp.route('/accounts', methods=['POST'])
def create_summoner():
    data = request.json
    accounts = data['accounts']

    # de-dupe the accounts
    names_set = set()
    accounts_cleaned = []
    for acc in accounts:
        if acc['summoner_name'] not in names_set:
            accounts_cleaned.append(acc)
        names_set.add(acc['summoner_name'])

    # update DB
    for account in accounts_cleaned:
        new_summoner = Summoner(
            ip=data['ip'],
            summoner_name=account['summoner_name'],
            tag_line=account['tag_line']
        )
        db.session.add(new_summoner)
    db.session.commit()  # must write all accounts for it to be a success

    return jsonify({'message': 'Summoner created successfully'}), 201


@summoner_bp.route('/accounts/<string:ip_address>', methods=['DELETE'])
def delete_accounts(ip_address):
    Summoner.query.filter_by(ip=ip_address).delete()
    db.session.commit()
    return jsonify({'message: ', 'Successfully deleted accounts'}), 200
