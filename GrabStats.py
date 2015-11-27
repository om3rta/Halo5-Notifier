from H5ArenaStats import H5ArenaStats


class GrabStats:

	def __init__(self):
		self.playlists_id = {"7b7e892c-d9b7-4b03-bef8-c6a071df28ef": "Free for All", "f27a65eb-2d11-4965-aa9c-daa088fa5c9c": "Swat",
				"f72e0ef0-7c4a-4307-af78-8e38dac3fdba": "Breakout", "892189e9-d712-4bdb-afa7-1ccab43fbed4": "Slayer", 
				"c98949ae-60a8-43dc-85d7-0feb0b92e719": "Team Arena"}

		self.designation = ["None", "Bronze", "Silver", "Gold", "Platinum", "Diamond", "Onyx", "Champion"]

	def last_game_info(self, user_name, api_key):
		stats = H5ArenaStats()
		last_game_id = stats.get_last_game_id(user_name, api_key)
		last_game_info = stats.get_report(last_game_id, api_key)
		playlist_id = last_game_info["PlaylistId"]
		playlist_name = self.playlists_id[playlist_id]
		game_info_dict = {"PlaylistId": playlist_id, "PlaylistName": playlist_name, "game_id": last_game_id}
		return game_info_dict

	def playlist_stats(self, playlist_id, user_name, api_key):
		stats = H5ArenaStats()
		service_record = stats.get_service_record(user_name, api_key)

		for player_info in service_record["Results"][0]["Result"]["ArenaStats"]["ArenaPlaylistStats"]:
			if player_info["PlaylistId"] == playlist_id:
				tier = player_info["Csr"]["Tier"]
				designation_id = player_info["Csr"]["DesignationId"]
				csr = player_info["Csr"]["Csr"]
				percent_to_next = player_info["Csr"]["PercentToNextTier"]
		
		designation_name = self.designation[designation_id]		
		playlist_info_dict = {"designation": designation_name, "tier": tier, "csr": csr, "progress": percent_to_next}
		return playlist_info_dict


#Call up last game stats
#post notification for that game type
#wait till last game id changes
#post notificaiton for that game type