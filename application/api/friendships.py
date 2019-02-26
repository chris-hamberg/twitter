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

class no_retweets(AbstractBase): 
    '''Returns a collection of user_ids that the currently authenticated user 
does not want to receive retweets from. 

Use POST friendships / update to set the “no retweets” status for a given user 
account on behalf of the current user. 

	- stringify_ids
	Many programming environments will not consume our ids due to their size. 
    Provide this option to have ids returned as strings instead. Read more about 
    [node:194]. This parameter is especially important to use in Javascript 
    environments.'''

    def __init__(self):
        super().__init__()
        self._endpoint += '/ids'
        self._url = self._url.split('.json')[0] + '/ids.json'
        self._method = get

    def __call__(self, stringify_ids=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 stringify_ids -> bool'''

class incoming(AbstractBase): 
    '''Returns a collection of numeric IDs for every user who has a pending 
request to follow the authenticating user. 

	- cursor
	Causes the list of connections to be broken into pages of no more than 5000 
    IDs at a time. The number of IDs returned is not guaranteed to be 5000 as 
    suspended users are filtered out after connections are queried. If no cursor 
    is provided, a value of -1 will be assumed, which is the first “page.” The 
    response from the API will include a previous_cursor and next_cursor to 
    allow paging back and forth. See [node:10362, title=”Using cursors to 
    navigate collections”] for more information. 

	- stringify_ids
	Many programming environments will not consume our Tweet ids due to their 
    size. Provide this option to have ids returned as strings instead. More 
    about [node:194].'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, cursor=None, stringify_ids=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 cursor        -> string
 stringify_ids -> bool'''

class outgoing(AbstractBase): 
    '''Returns a collection of numeric IDs for every protected user for whom the 
authenticating user has a pending follow request. 

	- cursor
	Causes the list of connections to be broken into pages of no more than 5000 
    IDs at a time. The number of IDs returned is not guaranteed to be 5000 as 
    suspended users are filtered out after connections are queried. If no cursor 
    is provided, a value of -1 will be assumed, which is the first “page.” The 
    response from the API will include a previous_cursor and next_cursor to 
    allow paging back and forth. See [node:10362, title=”Using cursors to 
    navigate collections”] for more information. 

	- stringify_ids
	Many programming environments will not consume our Tweet ids due to their 
    size. Provide this option to have ids returned as strings instead. More 
    about [node:194].'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, cursor=None, stringify_ids=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 cursor        -> string
 stringify_ids -> bool'''

class create(AbstractBase): 
    '''Allows the authenticating users to follow the user specified in the ID 
parameter. 

Returns the befriended user in the requested format when successful. Returns a 
string describing the failure condition when unsuccessful. If you are already 
friends with the user a HTTP 403 may be returned, though for performance reasons 
you may get a 200 OK message even if the friendship already exists. 

Actions taken in this method are asynchronous and changes will be eventually 
consistent. 

	- screen_name
	The screen name of the user for whom to befriend. 

	- user_id
	The ID of the user for whom to befriend. 

    - follow
	Enable notifications for the target user.'''
    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, screen_name=None, user_id=None, follow=False):
        return super().__call__(**filter(**vars(
            )))
    
    def __repr__(self):
        return '''PARAMETERS
 screen_name -> string
 user_id     -> int
 follow      -> bool'''

class destroy(AbstractBase): 
    '''Allows the authenticating user to unfollow the user specified in the ID 
parameter. 

Returns the unfollowed user in the requested format when successful. Returns a 
string describing the failure condition when unsuccessful. 

Actions taken in this method are asynchronous and changes will be eventually 
consistent. 

	- screen_name
	The screen name of the user for whom to unfollow. 

	- user_id
	The ID of the user for whom to unfollow.'''
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

class update(AbstractBase): 
    '''Allows one to enable or disable retweets and device notifications from 
the specified user. 

	- screen_name
	The screen name of the user for whom to befriend. 

	- user_id
	The ID of the user for whom to befriend. 

	- device
	Enable/disable device notifications from the target user. 

	- retweets
	Enable/disable retweets from the target user.'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, screen_name=None, user_id=None, device=False, 
            retweets=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 screen_name -> string
 user_id     -> int
 device      -> bool
 retweets    -> bool'''

class show(AbstractBase): 
    '''Returns detailed information about the relationship between two arbitrary 
users. 

	- source_id
	The user_id of the subject user. 

	- source_screen_name
	The screen_name of the subject user. 

	- target_id
	The user_id of the target user. 

	- target_screen_name
	The screen_name of the target user.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, source_id=None, source_screen_name=None, target_id=None, 
            target_screen_name=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 source_id          -> int; user id
 source_screen_name -> string; user name
 target_id          -> int; user id
 target_screen_name -> string; user name'''
     
class lookup(AbstractBase): 
    '''Returns the relationships of the authenticating user to the 
comma-separated list of up to 100 screen_names or user_ids provided. Values for 
connections can be: following, following_requested, followed_by, none, blocking, 
muting. 

	- screen_name
	A comma separated list of screen names, up to 100 are allowed in a single 
    request. 

	- user_id
	A comma separated list of user IDs, up to 100 are allowed in a single 
    request.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, screen_name=None, user_id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 screen_name -> string
 user_id     -> int'''
       
# encapsulate namespace
friendships = AbstractModule(globals())

# enforce singleton
del (no_retweets, incoming, outgoing, create, destroy, update, show, lookup,
     AbstractBase, AbstractModule, post, get)
