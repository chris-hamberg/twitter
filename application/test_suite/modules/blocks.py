from application.test_suite.modules.evaluate import evaluate

def test(twitter):

    ##########################################
    '''     Test the blocks.py module.     '''
    ##########################################

    twitter.blocks.List()
    twitter.blocks.ids()
    twitter.blocks.create('justinbeiber')
    twitter.blocks.destroy('justinbeiber')

    return evaluate(twitter, twitter.blocks)
