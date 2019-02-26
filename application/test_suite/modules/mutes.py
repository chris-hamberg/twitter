from application.test_suite.modules.evaluate import evaluate

def test(twitter):

    #########################################
    '''     Test the mutes.py module.     '''
    #########################################

    twitter.mutes.users.create(screen_name='RainmakerBeatz')
    twitter.mutes.users.ids()
    twitter.mutes.users.List()
    twitter.mutes.users.destroy(screen_name='RainmakerBeatz')

    return evaluate(twitter, twitter.mutes)
