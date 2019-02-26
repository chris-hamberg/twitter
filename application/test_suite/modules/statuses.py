from application.test_suite.modules.evaluate import evaluate
import random, time, json

def test(twitter):
    
    ##########################################
    '''    Test the statuses.py module.    '''
    ##########################################
    
    # special test parameter
    oembed = 'https://twitter.com/Interior/status/507185938620219395'
    tweet_id1 = 1033555529187172352
    tweet_id2 = 849813577770778624

    twitter.statuses.mentions_timeline()
    twitter.statuses.user_timeline(screen_name=twitter.username)
    twitter.statuses.home_timeline()
    twitter.statuses.retweets_of_me()
    twitter.statuses.retweets(id=tweet_id1)
    twitter.statuses.show(id=tweet_id2)
    twitter.statuses.retweet(id=tweet_id1)
    twitter.statuses.unretweet(id=tweet_id1)
    twitter.statuses.oembed(url=oembed)
    twitter.statuses.retweeters(id=tweet_id2)
    twitter.statuses.lookup(id=tweet_id2)
    twitter.statuses.update(status=random.randrange(1000, 1000000))
    tweet = None if twitter.mock else request(twitter)
    twitter.statuses.destroy(id=tweet)

    return evaluate(twitter, twitter.statuses)

def request(twitter):
    time.sleep(1)
    data = twitter.statuses.user_timeline(screen_name=twitter.username).json()
    return data[0]['id']
