from application.test_suite.modules.evaluate import evaluate

def test(twitter):

    ###########################################
    '''    Test the followers.py module.    '''
    ###########################################

    twitter.followers.ids(screen_name=twitter.username, count=1)
    twitter.followers.List(screen_name=twitter.username, count=1)

    return evaluate(twitter, twitter.followers)

