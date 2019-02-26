from application.test_suite.modules.evaluate import evaluate

def test(twitter):

    #########################################
    '''    Test the friends.py module.    '''
    #########################################

    twitter.friends.ids(screen_name=twitter.username, count=1)
    twitter.friends.List(screen_name=twitter.username, count=1)

    return evaluate(twitter, twitter.friends)

