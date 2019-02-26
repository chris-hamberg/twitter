from application.test_suite.modules.evaluate import evaluate

def test(twitter):
    
    ##########################################
    '''  Test the collections.py module.   '''
    ##########################################

    coll = 'test'
    if not twitter.mock:
        user = twitter.account.verify_credentials().json()['id']
        tweet = twitter.statuses.user_timeline(user).json()[0]['id']
        tweet2 = twitter.statuses.user_timeline.response.json()[1]['id']
        tweet3 = twitter.statuses.user_timeline.response.json()[2]['id']
    else:
        user = tweet = tweet2 = tweet3 = 'taco'

    twitter.collections.create(coll, timeline_order='curation_reverse_chron')
    twitter.collections.List(user)

    if not twitter.mock:
        id = list(twitter.collections.List.response.json()[
            'objects']['timelines'].keys(
            ))[0]
    else:
        id = 'taco'

    twitter.collections.entries_endpoint(id)
    twitter.collections.show(id)
    twitter.collections.entries.add(id, tweet_id=tweet)
    twitter.collections.entries.add(id=id, tweet_id=tweet2)
    twitter.collections.entries.curate(id=id, tweet_ids=[tweet3])
    twitter.collections.entries.move(id=id, tweet_id=tweet2, relative_to=tweet)
    twitter.collections.entries.remove(id=id, tweet_id=tweet)
    twitter.collections.update(id=id, name='test', description='...testing')
    twitter.collections.destroy(id=id)

    return evaluate(twitter, twitter.collections)
