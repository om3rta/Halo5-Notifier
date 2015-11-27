# Halo5-Notifier
Pops OS X notifications with info about your last Arena match

Halo5-Notifier does pretty much what the subtitle up above says it does. Once you run it, you'll get a notification with information about the last game you played, including what playlist you just played, what designation and tier you are in that playlist, and your progress towards the next tier or delegation. I wrote this because you're not told your progress towards ranking up in game, and the graphic representing progress on Halo Waypoint doesn't give you an exact percentage.

Requirements:

You should only need two things that don't come stock in Python/OS X, requests and terminal-notifier. Install requests with pip (pip install requests), and install terminal-notifier (brew install terminal notifier).

Running:

Add your api key to the api_key variable in run.py, then just run 'Python run.py "player name"' from wherever you clone the repository.

You can get an api key by signing up for a free developer account at https://developer.haloapi.com
