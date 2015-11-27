import requests
import sys
import json



class H5ArenaStats():

	def __init__(self):
		pass

	def get_service_record(self, user_name, api_key):
		"""
		gets the requested user's service reccord
		which can be used to look at CSR, and other
		stats for each arena playlist
		"""
		
		url = "https://www.haloapi.com/stats/h5/servicerecords/arena?players=" + str(user_name)
		headers = {'Ocp-Apim-Subscription-Key': api_key}
		r = requests.get(url, headers=headers)
		rr = r.json()
		return rr

	def get_last_game_id(self, user_name, api_key):
		"""
		gets the ID of the last game
		played by the specified player
		"""

		url = "https://www.haloapi.com/stats/h5/players/" + user_name + "/matches?modes=arena&count=1"
		headers = {'Ocp-Apim-Subscription-Key': api_key}
		r = requests.get(url, headers=headers)
		rr = r.json()
		game_id = rr["Results"][0]["Id"]["MatchId"]
		return game_id

	def get_report(self, match_id, api_key):
		"""
		grabs stats about a game
		by game ID
		"""

		url = "https://www.haloapi.com/stats/h5/arena/matches/" + match_id
		headers = {'Ocp-Apim-Subscription-Key': api_key}
		r = requests.get(url, headers=headers)
		rr = r.json()
		return rr