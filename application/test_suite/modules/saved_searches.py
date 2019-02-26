from application.test_suite.modules.evaluate import evaluate

def test(twitter):

    ##############################################
    '''   Test the saved_searches.py module.   '''
    ##############################################

    twitter.saved_searches.create(query='burrito')
    twitter.saved_searches.List()

    if not twitter.mock:
        id = twitter.saved_searches.List.response.json()[0]['id']
    else:
        id = '1'
    twitter.saved_searches.show(id)
    twitter.saved_searches.destroy(id)

    return evaluate(twitter, twitter.saved_searches)
