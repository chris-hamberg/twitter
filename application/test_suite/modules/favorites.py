from application.test_suite.modules.evaluate import evaluate

def test(twitter):

    ###########################################
    '''    Test the favorites.py module.    '''
    ###########################################

    twitter.favorites.List()
    twitter.favorites.create(729136456090963968)
    twitter.favorites.destroy(729136456090963968)

    return evaluate(twitter, twitter.favorites)
