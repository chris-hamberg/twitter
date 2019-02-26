from application.test_suite.modules.evaluate import evaluate

def test(twitter):
    
    #######################################
    '''    Test the lists.py module.    '''
    #######################################

    twitter.lists.create(name='test', mode='private', description='tacos')

    twitter.lists.List()

    if not twitter.mock:
        list_id = twitter.lists.List.response.json()[0]['id']
    else:
        list_id = '1'
    
    twitter.lists.statuses(list_id)
    twitter.lists.memberships(screen_name=twitter.username)
    twitter.lists.subscribers_endpoint(list_id)
    twitter.lists.members_endpoint(list_id)
    twitter.lists.update(list_id, description='burritos')
    twitter.lists.show(list_id)
    twitter.lists.subscriptions(screen_name=twitter.username)
    twitter.lists.ownerships(screen_name=twitter.username)

    #NOTE lists/members
    ###################
    twitter.lists.members.create(list_id=list_id, screen_name='MegaDopeBeatz')
    twitter.lists.members.create_all(list_id=list_id, 
            screen_name='RainmakerBeatz,')
    twitter.lists.members.show(list_id=list_id, screen_name='MegaDopeBeatz')
    twitter.lists.members.destroy(list_id=list_id, screen_name='MegaDopeBeatz')
    twitter.lists.members.destroy_all(list_id=list_id, 
            screen_name='RainmakerBeatz,')
    
    twitter.lists.destroy(list_id=list_id)

    #NOTE lists/subscribers
    #######################
    list_id = 102476661
    twitter.lists.subscribers.create(list_id=list_id)
    twitter.lists.subscribers.show(list_id=list_id, 
            screen_name=twitter.username)
    twitter.lists.subscribers.destroy(list_id=list_id)

    return evaluate(twitter, twitter.lists)
