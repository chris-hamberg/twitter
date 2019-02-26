from application.test_suite.modules.evaluate import evaluate
from application.subprocess.subroutines import locator
import os

def test(twitter):
    
    ##########################################
    '''    Test the accounts.py module.    '''
    ##########################################

    relpath = os.path.join('application', 'test_suite', 'resources')

    twitter.account.settings()
    twitter.account.verify_credentials()
    twitter.account.update_settings(sleep_time_enabled='true')
    twitter.account.update_settings(sleep_time_enabled='false')
    twitter.account.update_profile(name='FishBall1796')
    twitter.account.update_profile(name=twitter.username)
    image = locator(os.path.join(relpath, '_test_img.jpg'))
    twitter.account.update_profile_image(image=image)
    image = locator(os.path.join(relpath, 'test_img.jpg'))
    twitter.account.update_profile_image(image=image)
    image = locator(os.path.join(relpath, 'test_banner.png'))
    twitter.account.update_profile_banner(banner=image)
    twitter.account.remove_profile_banner()

    return evaluate(twitter, twitter.account)
