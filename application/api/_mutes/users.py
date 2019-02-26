try:
    from twitter.application.api.superclass.abstract_module import AbstractModule
    from twitter.application.api.superclass.superclasses import Ternary
    from twitter.application.subprocess.subroutines import filter
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_module import AbstractModule
    from application.api.superclass.superclasses import Ternary
    from application.subprocess.subroutines import filter
finally:    
    from requests import post, get

class create(Ternary): 
    '''Mutes the user specified in the ID parameter for the authenticating user. 

Returns the muted user in the requested format when successful. Returns a string 
describing the failure condition when unsuccessful. 

Actions taken in this method are asynchronous and changes will be eventually 
consistent. 

	- screen_name
	The screen name of the potentially muted user. Helpful for disambiguating 
    when a valid screen name is also a user ID. 

	- user_id
	The ID of the potentially muted user. Helpful for disambiguating when a 
    valid user ID is also a valid screen name.'''
    
    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, screen_name=None, user_id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 screen_name -> string
 user_id     -> int'''

class destroy(Ternary): 
    '''Un-mutes the user specified in the ID parameter for the authenticating 
user. 

Returns the unmuted user in the requested format when successful. Returns a 
string describing the failure condition when unsuccessful. 

Actions taken in this method are asynchronous and changes will be eventually 
consistent. 

	- screen_name
	The screen name of the potentially muted user. Helpful for disambiguating 
    when a valid screen name is also a user ID. 

	- user_id
	The ID of the potentially muted user. Helpful for disambiguating when a 
    valid user ID is also a valid screen name.'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, screen_name=None, user_id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 screen_name -> string
 user_id     -> int'''

class ids(Ternary): 
    '''Returns an array of numeric user ids the authenticating user has muted. 

	- cursor
	Causes the list of IDs to be broken into pages of no more than 5000 IDs at a 
    time. The number of IDs returned is not guaranteed to be 5000 as suspended 
    users are filtered out. If no cursor is provided, a value of -1 will be 
    assumed, which is the first “page.” The response from the API will include a 
    previous_cursor and next_cursor to allow paging back and forth. See 
    [node:10362, title=”Using cursors to navigate collections”] for more 
	information.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, cursor=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 cursor -> string'''

class List(Ternary): 
    '''Returns an array of user objects the authenticating user has muted. 

	- cursor
	Causes the list of IDs to be broken into pages of no more than 5000 IDs at a 
    time. The number of IDs returned is not guaranteed to be 5000 as suspended 
    users are filtered out after connections are queried. If no cursor is 
    provided, a value of -1 will be assumed, which is the first “page.” The 
    response from the API will include a previous_cursor and next_cursor to 
    allow paging back and forth. See [node:10362, title=”Using cursors to 
    navigate collections”] for more information. 

	- include_entities
    The entities node will not be included when set to false. 

	- skip_status
	When set to either true, t or 1 statuses will not be included in the 
    returned user objects.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, cursor=None, include_entities=False, 
            skip_status=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 cursor           -> string
 include_entities -> bool'''

# encapsulate namespace
users = AbstractModule(globals())

# enforce singleton
del (create, destroy, ids, List,
     Ternary, AbstractModule, post, get)
