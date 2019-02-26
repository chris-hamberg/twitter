from application.test_suite.modules.evaluate import evaluate

def test(twitter):

    #########################################
    '''      Test the geo.py module.      '''
    #########################################

    twitter.geo.reverse_geocode(37, 122)
    twitter.geo.id('00bc52ea1fc46565')
    twitter.geo.search(query='cincinnati')

    return evaluate(twitter, twitter.geo)
