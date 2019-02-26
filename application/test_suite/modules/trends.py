from application.test_suite.modules.evaluate import evaluate

def test(twitter):

    ########################################
    '''    Test the trends.py module.    '''
    ########################################

    twitter.trends.available()
    if not twitter.mock:
        id = twitter.trends.available.response.json()[0]['woeid']
    else:
        id = 1
    twitter.trends.place(id=id)
    twitter.trends.closest(lat=37, long=100)

    return evaluate(twitter, twitter.trends)
