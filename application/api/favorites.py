try:
    from twitter.application.api.superclass.abstract_base_class import AbstractBase
    from twitter.application.api.superclass.abstract_module import AbstractModule
    from twitter.application.subprocess.subroutines import filter
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_base_class import AbstractBase
    from application.api.superclass.abstract_module import AbstractModule
    from application.subprocess.subroutines import filter
finally:
    from requests import post, get

#NOTE favorites are now known as likes

class List(AbstractBase): 
    '''Returns the 20 most recent Tweets liked by the authenticating or 
specified user. 

Note: the like action was known as favorite before November 3, 2015; the 
historical naming remains in API methods and object properties. 

	- user_id
	The ID of the user for whom to return results for. 

	- screen_name
	The screen name of the user for whom to return results for. 

	- count
	Specifies the number of records to retrieve. Must be less than or equal to 
    200; defaults to 20. The value of count is best thought of as a limit to the 
    number of tweets to return because suspended or deleted content is removed 
    after the count has been applied. 

	- since_id
	Returns results with an ID greater than (that is, more recent than) the 
    specified ID. There are limits to the number of Tweets which can be accessed 
    through the API. If the limit of Tweets has occured since the since_id, 
    the since_id will be forced to the oldest ID available. 

	- max_id
	Returns results with an ID less than (that is, older than) or equal to the 
    specified ID. 

	- include_entities
	The entities node will be omitted when set to false.'''
    
    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, user_id=None, screen_name=None, count=20, since_id=None, 
            max_id=None, include_entities=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
user_id          -> int
screen_name      -> string
count            -> int
since_id         -> int
max_id           -> int
include_entities -> bool'''

class destroy(AbstractBase): 
    '''Note: the like action was known as favorite before November 3, 2015; the 
historical naming remains in API methods and object properties. 

Un-likes the status specified in the ID parameter as the authenticating user. 
Returns the un-liked status in the requested format when successful. 

This process invoked by this method is asynchronous. The immediately returned 
status may not indicate the resultant liked status of the Tweet. A 200 OK 
response from this method will indicate whether the intended action was 
successful or not. 

	- id
	The numerical ID of the desired status. 

	- include_entities
	The entities node will be omitted when set to false.'''
    
    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, id=None, include_entities=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 id               -> int; status id
 include_entities -> bool'''

class create(AbstractBase): 
    '''Note: the like action was known as favorite before November 3, 2015; the 
historical naming remains in API methods and object properties. 

Likes the status specified in the ID parameter as the authenticating user. 
Returns the liked status when successful. 

This process invoked by this method is asynchronous. The immediately returned 
status may not indicate the resultant liked status of the tweet. A 200 OK 
response from this method will indicate whether the intended action was 
successful or not. 

	- id
	The numerical ID of the desired status. 

	- include_entities
	The entities node will be omitted when set to false.'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, id=None, include_entities=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 id               -> int; status id
 include_entities -> bool'''

# encapsulate namespace
favorites = AbstractModule(globals())

# enforce singleton
del (List, destroy, create,
     AbstractBase, AbstractModule, post, get)
