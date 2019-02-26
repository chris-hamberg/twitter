from application.test_suite.modules.evaluate import evaluate
from application.subprocess.subroutines import locator
import random, os

def test(twitter):

    #########################################
    '''     Test the media.py module.     '''
    #########################################

    relpath = os.path.join('application', 'test_suite', 'resources')
    fname = 'test_img.jpg'
    image = locator(os.path.join(relpath, fname))

    twitter.media.upload(image=image)

    return evaluate(twitter, twitter.media)
