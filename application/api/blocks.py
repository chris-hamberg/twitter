try:
    from twitter.application.api.superclass.abstract_base_class import AbstractBase
    from twitter.application.api.superclass.abstract_module import AbstractModule
    from twitter.application.subprocess.subroutines import filter
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_base_class import AbstractBase
    from application.api.superclass.abstract_module import AbstractModule
    from application.subprocess.subroutines import filter
finally:
    from requests import get, post
   
class List(AbstractBase): 
    '''Returns a collection of user objects that the authenticating user is 
blocking. 

Important This method is cursored, meaning your app must make multiple requests 
in order to receive all blocks correctly. See Using cursors to navigate 
collections for more details on how cursoring works. 

	- include_entities
	The entities node will not be included when set to false. 

	- skip_status
	When set to either true, t or 1 statuses will not be included in the 
    returned user objects. 

	- cursor
	Causes the list of blocked users to be broken into pages of no more than 
    5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 
    as suspended users are filtered out after connections are queried. If no 
    cursor is provided, a value of -1 will be assumed, which is the first 
    “page.” The response from the API will include a previous_cursor and 
    next_cursor to allow paging back and forth. See Using cursors to navigate 
    collections for more information.'''
    
    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, include_entities=False, skip_status=False, cursor=-1):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 include_entities -> bool
 skip_status      -> true, t or 1
 cursor           -> int'''

class ids(AbstractBase): 
    '''Returns an array of numeric user ids the authenticating user is blocking.

Important This method is cursored, meaning your app must make multiple 
requests in order to receive all blocks correctly. See Using cursors to 
navigate collections for more details on how cursoring works. 

	- stringify_ids
	Many programming environments will not consume our ids due to their size. 
    Provide this option to have ids returned as strings instead. Read more about 
    Twitter IDs. 

	- cursor
	Causes the list of IDs to be broken into pages of no more than 5000 IDs at 
    a time. The number of IDs returned is not guaranteed to be 5000 as suspended 
    users are filtered out after connections are queried. If no cursor is 
    provided, a value of -1 will be assumed, which is the first “page.” The 
    response from the API will include a previous_cursor and next_cursor to 
    allow paging back and forth. See Using cursors to navigate collections for 
    more information.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, stringify_ids=False, cursor=-1):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 stringify_ids -> bool
 cursor        -> int'''
    
class create(AbstractBase): 
    '''Blocks the specified user from following the authenticating user. In 
addition the blocked user will not show in the authenticating users mentions or 
timeline (unless retweeted by another user). If a follow or friend relationship 
exists it is destroyed. 

The URL pattern /version/block/create/:screen_name_or_user_id.format is still 
accepted but not recommended. As a sequence of numbers is a valid screen name we 
recommend using the screen_name or user_id parameter instead. 

    - screen_name
	The screen name of the potentially blocked user. Helpful for disambiguating 
    when a valid screen name is also a user ID. 

	- user_id
	The ID of the potentially blocked user. Helpful for disambiguating when a 
    valid user ID is also a valid screen name. 

	- include_entities
	The entities node will not be included when set to false. 

    - skip_status
	When set to either true, t or 1 statuses will not be included in the 
    returned user objects.'''

    def __init__(self):
        super().__init__()
        self._method = post
   
    def __call__(self, screen_name=None, user_id=None, include_entities=False,
            skip_status=False):
        super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 screen_name      -> string
 user_id          -> int; user id
 include_entities -> bool
 skip_status      -> true, t or 1'''

class destroy(AbstractBase): 
    '''Un-blocks the user specified in the ID parameter for the 
authenticating user. Returns the un-blocked user in the requested format when 
successful. If relationships existed before the block was instated, they will 
not be restored. 

	- screen_name
	The screen name of the potentially blocked user. Helpful for disambiguating 
    when a valid screen name is also a user ID. 

    - user_id
	The ID of the potentially blocked user. Helpful for disambiguating when a 
    valid user ID is also a valid screen name. 

	- include_entities
	The entities node will not be included when set to false. 

    - skip_status
	When set to either true, t or 1 statuses will not be included in the 
    returned user objects.'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, screen_name=None, user_id=None, include_entities=True, 
            skip_status=False):
        super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 screen_name      -> string
 user_id          -> int; twitter user id
 include_entities -> bool
 skip_status      -> bool'''

# encapsulate namespace
blocks = AbstractModule(globals())

# enforce singleton

del (List, ids, create, destroy,

     AbstractBase, AbstractModule, get, post)
