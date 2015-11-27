from H5ArenaStats import H5ArenaStats
from GrabStats import GrabStats
from BuildNotification import BuildNotification
import time
import sys

user_name = sys.argv[1]
api_key = ""

grab = GrabStats()
stats = grab.last_game_info(user_name, api_key)
notify = BuildNotification()

last_playlist = grab.playlist_stats(stats["PlaylistId"], user_name, api_key)

icon = str(last_playlist["designation"]) + str(last_playlist["tier"]) + ".png"
if last_playlist["designation_id"] < 6:
	rank = last_playlist["designation"] + " " + str(last_playlist["tier"])
	progress = last_playlist["progress"]
	icon = str(last_playlist["designation"]) + str(last_playlist["tier"]) + ".png"
	onyxchamp = False
else:
	rank = last_playlist["designation"]
	progress = last_playlist["csr"]
	icon = str(last_playlist["designation"]) + ".png"
	onyxchamp = True

send_notification = notify.send_notification(stats["PlaylistName"], icon, progress, user_name, rank, onyxchamp)

current_id = stats["PlaylistId"]
new_id = stats["PlaylistId"]
keepalive = True
while keepalive == True:
	while new_id == current_id:
		time.sleep(5)
		new_id_lookup = grab.last_game_info(user_name, api_key)
		new_id = new_id_lookup["PlaylistId"]
	
	current_id = new_id
	stats = grab.last_game_info(user_name, api_key)	
	last_playlist = grab.playlist_stats(stats["PlaylistId"], user_name, api_key)
	send_notification = notify.send_notification(stats["PlaylistName"], icon, last_playlist["progress"], user_name, rank)
