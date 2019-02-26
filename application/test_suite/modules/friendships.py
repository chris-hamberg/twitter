from application.test_suite.modules.evaluate import evaluate
from application.extras.containers import MockResponse

def test(twitter):

    #########################################
    '''    Test the friends.py module.    '''
    #########################################

    twitter.friendships.no_retweets()
    twitter.friendships.incoming()
    twitter.friendships.outgoing()
    twitter.friendships.create(screen_name='MegaDopeBeatz')
    twitter.friendships.update(screen_name='MegaDopeBeatz', device=True)
    twitter.friendships.show(source_screen_name=twitter.username, 
            target_screen_name='MegaDopeBeatz')
    twitter.friendships.lookup('MegaDopeBeatz, RainmakerBeatz')
    #twitter.friendships.destroy(screen_name='MegaDopeBeatz')
    twitter.friendships.destroy._response = MockResponse('place holder')

    return evaluate(twitter, twitter.friendships)
