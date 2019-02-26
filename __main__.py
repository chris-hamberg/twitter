from application.subprocess.subroutines import clear
from application.extras.banner import banner
from twitter import Twitter
import application.interactive.session

clear(); print(banner)
twitter = Twitter()
application.interactive.session.twitter = twitter
application.interactive.session.execute()
