from application.test_suite.modules.evaluate import evaluate

def test(twitter):

    #############################################
    '''    Test the application.py module.    '''
    #############################################

    twitter.application.rate_limit_status()

    return evaluate(twitter, twitter.application)
