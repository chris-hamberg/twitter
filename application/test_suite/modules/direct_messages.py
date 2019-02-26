from application.extras.containers import MockResponse
from application.test_suite.modules.evaluate import evaluate
import random, time

def test(twitter):

    ###########################################
    ''' Test the direct_messages.py module. '''
    ###########################################
    
    message = random.randrange(10**10, 10**12)

    twitter.direct_messages.events.show(id=731251362084835331)
    twitter.direct_messages.events.new(id=1351344822, text=message)
    twitter.direct_messages.events.List()
    
    #NOTE can't be automatically tested
    ##### requires an inbox message
    ##### twitter.direct_messages.destroy(id)
    twitter.direct_messages.events.destroy._response = MockResponse('place holder')

    twitter.direct_messages.mark_read(last_read_event_id=1037162521319415814, 
            recipient_id=1351344822)
    twitter.direct_messages.indicate_typing(recipient_id=1351344822)


    return evaluate(twitter, twitter.direct_messages)
