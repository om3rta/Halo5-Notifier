import os



class BuildNotification():

	def __init__(self):
		self.icon = ""

	def send_notification(self, playlist, icon, percentage, user_name, rank, onyxchamp):

		icon_path = os.getcwd() + "/icon_set/"
		notifier_path = '/Applications/terminal-notifier.app/Contents/MacOS/terminal-notifier '
		message_title = "-title '" + playlist  + " info for " + user_name + "' "
		message_subtitle = "-subtitle '" + rank + "' "
		if onyxchamp == False:
			message_body =  "-message 'Percent to next: " + str(percentage) + "%' "
		else:
			message_body =  "-message 'CSR: " + str(percentage) + "' "
		app_image = "-contentImage " + icon_path + icon
		app_icon = "-appIcon " + icon_path + "5.png " 

		sendnotificaiton = os.system(str(notifier_path) + str(message_title) + str(message_subtitle) + str(message_body) + str(app_icon) +  str(app_image))