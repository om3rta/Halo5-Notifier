from H5ArenaStats import H5ArenaStats
from GrabStats import GrabStats
from BuildNotification import BuildNotification
import time
import sys
import os

user_name = raw_input("Track games for which user?: ")


#get the api key
api_key = ""
key_location = os.getcwd() + "/apikey.txt"
if os.path.isfile(key_location) == True:
	open_file = open(key_location, "r")
	api_key = open_file.read()
	grab = GrabStats()
	stats = grab.last_game_info(user_name, api_key)
	notify = BuildNotification()
	last_playlist = grab.playlist_stats(stats["PlaylistId"], user_name, api_key)
else:
	key_ready = False
	while key_ready == False:
		print "\nApi key missing or incorrect."
		api_key = raw_input("Enter your api key: ")
		print "Let me check that right quick..."
		try:
			grab = GrabStats()
			stats = grab.last_game_info(user_name, api_key)
			notify = BuildNotification()
			last_playlist = grab.playlist_stats(stats["PlaylistId"], user_name, api_key)
			api_key_file = open("apikey.txt", "w+")
			api_key_file.write(api_key)
			api_key_file.close()
			print "\nApi key recorded. All set."
			key_ready = True
		except:
			pass

#api_key = "ecbe0ddbe57246c4bf82cd0f4f3be301"

#Send first notification
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

#Notification loop
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
		send_notification = notify.send_notification(stats["PlaylistName"], icon, last_playlist["progress"], user_name, rank)