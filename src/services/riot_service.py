import requests
from config import RIOT_API_KEY

base_url = "https://americas.api.riotgames.com/"


def call(url):
    headers = {"X-Riot-Token": RIOT_API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()


def get_summoner_data(summoner_name, tag_line):
    url = f"{base_url}/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tag_line}"
    return call(url)


def get_matches(puuid):
    url = f"{base_url}/lol/match/v5/matches/by-puuid/{puuid}/ids"
    return call(url)


def get_match(match_id):
    url = f"{base_url}/lol/match/v5/matches/{match_id}"
    return call(url)