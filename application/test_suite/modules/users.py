from application.test_suite.modules.evaluate import evaluate

def test(twitter):

    ##########################################
    '''     Test the users.py module.      '''
    ##########################################

    twitter.users.lookup(screen_name='MegaDopeBeatz,')
    twitter.users.show(screen_name='MegaDopeBeatz')
    twitter.users.search(q='burrito')
    twitter.users.profile_banner(screen_name='MegaDopeBeatz')
    twitter.users.suggestions_endpoint()
    twitter.users.report_spam(screen_name='JustinBeiber')

    # NOTE suggestions
    ##################
    twitter.users.suggestions.slug('music')
    twitter.users.suggestions.members('music')

    return evaluate(twitter, twitter.users)
