try:
    from twitter.application.api.superclass.abstract_base_class import AbstractBase
    from twitter.application.api.superclass.abstract_module import AbstractModule
    from twitter.application.api.superclass.superclasses import Collision
    from twitter.application.subprocess.subroutines import filter
    from twitter.application.api._collections.entries import entries
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_base_class import AbstractBase
    from application.api.superclass.abstract_module import AbstractModule
    from application.api.superclass.superclasses import Collision
    from application.subprocess.subroutines import filter
    from application.api._collections.entries import entries
finally:
    from requests import get, post

class entries_endpoint(Collision):
    '''Retrieve the identified Collection, presented as a list of the Tweets 
curated within. 

The response structure of this method differs significantly from timelines you 
may be used to working with elsewhere in the Twitter API.

To navigate a Collection, use the position object of a response, which includes 
attributes for max_position, min_position, and was_truncated. was_truncated 
indicates whether additional Tweets exist in the collection outside of the range 
of the current request. To retrieve Tweets further back in time, use the value 
of min_position found in the current response as the max_position parameter in 
the next call to this endpoint.

    - id
    The identifier of the Collection for which to return results.	 	

    - count	
    Specifies the maximum number of results to include in the response. Specify 
    a count between 1 and 200. A next_cursor value will be provided in the 
    response if additional results are available.

    - max_position
    Returns results with a position value less than or equal to the specified 
    position.

    - min_position
    Returns results with a position greater than the specified position.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, id=None, count=20, max_position=None, min_position=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 id           -> string
 count        -> 1 <= int <= 200
 max_position -> int
 min_position -> int'''

class List(AbstractBase):
    '''Find Collections created by a specific user or containing a specific 
curated Tweet.

Results are organized in a cursored collection.

    - user_id
    The ID of the user for whom to return results.

    - screen_name
    The screen name of the user for whom to return results.

    - tweet_id
    The identifier of the Tweet for which to return results.

    - count
    Specifies the maximum number of results to include in the response. Specify 
    a count between 1 and 200. A next_cursor value will be provided in the 
    response if additional results are available.

    - cursor
    A string identifying the segment of the current result set to retrieve. 
    Values for this parameter are yielded in the cursors node attached to 
    response objects. Usage of the count parameter affects cursoring.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, user_id=None, screen_name=None, tweet_id=None, count=20,
            cursor=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 user_id -> int
 screen_name -> string
 tweet_id -> int
 count -> 1 <= int <= 200
 cursor -> string; segment ID'''

class show(AbstractBase):
    '''Retrieve information associated with a specific Collection.
         
    - id
    The identifier of the Collection for which to return results.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''
 id -> string; collection ID'''

class create(AbstractBase):
    '''Create a Collection owned by the currently authenticated user.

The API endpoint may refuse to complete the request if the authenticated user 
has exceeded the total number of allowed collections for their account.

    - name
    The title of the collection being created, in 25 characters or less.

    - description
    A brief description of this collection in 160 characters or fewer.

    - url
    A fully-qualified URL to associate with this collection.

    - timeline_order
    Order Tweets chronologically or in the order they are added to a Collection. 
    curation_reverse_chron - order added (default) tweet_chron - oldest first 
    tweet_reverse_chron - most recent first'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, name=None, description=None, url=None, 
            timeline_order=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 name           -> string
 description    -> string
 url            -> string
 timeline_order -> {'curation_reverse_chron', 'tweet_chron', 
                    'tweet_reverse_chron'}'''

class destroy(AbstractBase):
    '''Permanently delete a Collection owned by the currently authenticated 
user.

    - id
    The identifier of the Collection to destroy.'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 id -> string'''

class update(AbstractBase):
    '''Update information concerning a Collection owned by the currently 
authenticated user.

Partial updates are not currently supported: please provide name, description, 
and url whenever using this method. Omitted description or url parameters will 
be treated as if an empty string was passed, overwriting any previously stored 
value for the Collection.
        
    - id
    The identifier of the Collection to modify.

    - name
    The title of the Collection being created, in 25 characters or fewer.

    - description
    A brief description of this Collection in 160 characters or fewer.

    - url
    A fully-qualified URL to associate with this Collection.'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, id=None, name=None, description=None, url=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 id          -> string
 name        -> string
 description -> string
 url         -> string'''

# encapsulate
collections = AbstractModule(globals())
setattr(collections, 'entries', entries)

# enforce singleton
del (entries, List, show, create, destroy, entries_endpoint,
        
     AbstractBase, AbstractModule, Collision, post, get)
