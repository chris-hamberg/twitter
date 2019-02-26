try:
    from twitter.application.api.superclass.abstract_base_class import AbstractBase
    from twitter.application.api.superclass.abstract_module import AbstractModule
    from twitter.application.api.superclass.superclasses import Empty
    from twitter.application.subprocess.subroutines import filter
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_base_class import AbstractBase
    from application.api.superclass.abstract_module import AbstractModule
    from application.api.superclass.superclasses import Empty
    from application.subprocess.subroutines import filter
finally:    
    from requests import get

class place(AbstractBase): 
    '''Returns the top 50 trending topics for a specific WOEID, if trending 
information is available for it. 

The response is an array of “trend” objects that encode the name of the trending 
topic, the query parameter that can be used to search for the topic on Twitter 
Search, and the Twitter Search URL. 

This information is cached for 5 minutes. Requesting more frequently than that 
will not return any more data, and will count against your rate limit usage. 

The tweet volume (tweet_volume) for the last 24 hours is also returned for every 
trend. 

Please note that Ads API developers have an increased rate limit on this 
endpoint at 50 queries / 15 minutes / token. 

	- id
	The Yahoo! Where On Earth ID of the location to return trending information 
    for. Global information is available by using 1 as the WOEID. 

	- exclude
	Setting this equal to hashtags will remove all hashtags from the trends 
    list.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, id=None, exclude=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 id      -> Yahoo! WOEID
 exclude -> 'hashtags' (logically equivalent to False)'''

class available(Empty): 
    '''Returns the locations that Twitter has trending topic information for. 

The response is an array of “locations” that encode the location’s WOEID and 
some other human-readable information such as a canonical name and country the 
location belongs in. 

A WOEID is a Yahoo! Where On Earth ID.'''

    def __init__(self):
        super().__init__()
        self._method = get

class closest(AbstractBase): 
    '''Returns the locations that Twitter has trending topic information for, 
closest to a specified location. 

The response is an array of “locations” that encode the location’s WOEID and 
some other human-readable information such as a canonical name and country the 
location belongs in. 

A WOEID is a Yahoo! Where On Earth ID. 

	- lat
	If provided with a long parameter the available trend locations will be 
    sorted by distance, nearest to furthest, to the co-ordinate pair. The valid 
    ranges for longitude is -180.0 to +180.0 (West is negative, East is 
    positive) inclusive. 

	- long
	If provided with a lat parameter the available trend locations will be 
    sorted by distance, nearest to furthest, to the co-ordinate pair. The valid 
    ranges for longitude is -180.0 to +180.0 (West is negative, East is 
    positive) inclusive.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, lat=None, long=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 lat  -> -90 <= int <= 90
 long -> -180 <= int <= 180'''

# encapsulate namespace
trends = AbstractModule(globals())

# enforce singleton
del (place, available, closest,
     AbstractBase, AbstractModule, Empty, get)
