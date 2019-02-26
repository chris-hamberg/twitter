try:
    from twitter.application.api.superclass.abstract_base_class import AbstractBase
    from twitter.application.api.superclass.abstract_module import AbstractModule
    from twitter.application.api.superclass.superclasses import Collision
    from twitter.application.api._lists.subscribers import subscribers
    from twitter.application.subprocess.subroutines import filter
    from twitter.application.api._lists.members import members
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_base_class import AbstractBase
    from application.api.superclass.abstract_module import AbstractModule
    from application.api.superclass.superclasses import Collision
    from application.api._lists.subscribers import subscribers
    from application.subprocess.subroutines import filter
    from application.api._lists.members import members
finally:
    from requests import post, get

class List(AbstractBase): 
    '''Returns all lists the authenticating or specified user subscribes to, 
including their own. The user is specified using the user_id or screen_name 
parameters. If no user is given, the authenticating user is used. 

This method used to be GET lists in version 1.0 of the API and has been renamed 
for consistency with other call. 

A maximum of 100 results will be returned by this call. Subscribed lists are 
returned first, followed by owned lists. This means that if a user subscribes to 
90 lists and owns 20 lists, this method returns 90 subscriptions and 10 owned 
lists. The reverse method returns owned lists first, so with reverse=true, 20 
owned lists and 80 subscriptions would be returned. If your goal is to obtain 
every list a user owns or subscribes to, use GET lists / ownerships and/or GET 
lists / subscriptions instead. 

	- user_id
	The ID of the user for whom to return results for. Helpful for 
    disambiguating when a valid user ID is also a valid screen name. Note: 
    Specifies the ID of the user to get lists from. Helpful for disambiguating 
    when a valid user ID is also a valid screen name. 

	- screen_name
	The screen name of the user for whom to return results for. Helpful for 
    disambiguating when a valid screen name is also a user ID. 

	- reverse
	Set this to true if you would like owned lists to be returned first. See 
    description above for information on how this parameter works.'''
    
    def __init__(self):
        super().__init__()
        self._method = get 

    def __call__(self, user_id=None, screen_name=None, reverse=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 user_id     -> int
 screen_name -> string
 reverse     -> bool'''

class statuses(AbstractBase): 
    '''Returns a timeline of tweets authored by members of the specified list. 
Retweets are included by default. Use the include_rts=false parameter to omit 
retweets. 

Embedded Timelines is a great way to embed list timelines on your website. 

	- list_id
	The numerical id of the list. 

	- slug
	You can identify a list by its slug instead of its numerical id. If you 
    decide to do so, note that you’ll also have to specify the list owner using 
    the owner_id or owner_screen_name parameters. 

	- owner_screen_name
	The screen name of the user who owns the list being requested by a slug. 

	- owner_id
	The user ID of the user who owns the list being requested by a slug. 
		
    - since_id
	Returns results with an ID greater than (that is, more recent than) the 
    specified ID. There are limits to the number of Tweets which can be accessed 
    through the API. If the limit of Tweets has occured since the since_id, the 
    since_id will be forced to the oldest ID available. 

	- max_id
	Returns results with an ID less than (that is, older than) or equal to the 
    specified ID. 

	- count
	Specifies the number of results to retrieve per “page.” 

	- include_entities
	Entities are ON by default in API 1.1, each tweet includes a node called 
    “entities”. This node offers a variety of metadata about the tweet in a 
    discrete structure, including: user_mentions, urls, and hashtags. You can 
    omit entities from the result by using include_entities=false 

	- include_rts
	When set to either true, t or 1, the list timeline will contain native 
    retweets (if they exist) in addition to the standard stream of tweets. The 
    output format of retweeted tweets is identical to the representation you see 
    in home_timeline.'''

    def __init__(self):
        super().__init__()
        self._method = get 

    def __call__(self, list_id=None, slug=None, owner_screen_name=None, 
            owner_id=None, since_id=None, max_id=None, count=20, 
            include_rts=False, include_entities=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 list_id           -> int
 slug              -> string
 owner_screen_name -> string
 owner_id          -> int
 since_id          -> int; tweet id
 max_id            -> int; tweet id
 count             -> int
 include_rts       -> bool
 include_entities  -> bool'''

class memberships(AbstractBase): 
    '''Returns the lists the specified user has been added to. If user_id or 
screen_name are not provided the memberships for the authenticating user are 
returned. 

	- user_id
	The ID of the user for whom to return results for. Helpful for 
    disambiguating when a valid user ID is also a valid screen name. 

	- screen_name
	The screen name of the user for whom to return results for. Helpful for 
    disambiguating when a valid screen name is also a user ID. 

	- count
	The amount of results to return per page. Defaults to 20. No more than 1000 
    results will ever be returned in a single page. 

	- cursor
	Breaks the results into pages. Provide a value of -1 to begin paging. 
    Provide values as returned in the response body’s next_cursor and 
    previous_cursor attributes to page back and forth in the list. It is 
    recommended to always use cursors when the method supports them. See 
    [node:10362] for more information. 

	- filter_to_owned_lists
	When set to true, t or 1, will return just lists the authenticating user 
    owns, and the user represented by user_id or screen_name is a member of.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, user_id=None, screen_name=None, count=20, cursor=None, 
            filter_to_owned_lists=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 user_id               -> int
 screen_name           -> string
 count                 -> int <= 1000
 cursor                -> string
 filter_to_owned_lists -> bool'''

class subscribers_endpoint(Collision): 
    '''Returns the subscribers of the specified list. Private list subscribers 
will only be shown if the authenticated user owns the specified list. 

	- list_id
	The numerical id of the list. 

	- slug
	You can identify a list by its slug instead of its numerical id. If you 
    decide to do so, note that you’ll also have to specify the list owner using 
    the owner_id or owner_screen_name parameters. 

	- owner_screen_name
	The screen name of the user who owns the list being requested by a slug. 

	- owner_id
	The user ID of the user who owns the list being requested by a slug. 

	- count
	Specifies the number of results to return per page (see cursor below). The 
    default is 20, with a maximum of 5,000. 

	- cursor
	Breaks the results into pages. A single page contains 20 lists. Provide a 
    value of -1 to begin paging. Provide values as returned in the response 
    body’s next_cursor and previous_cursor attributes to page back and forth in 
    the list. See Using cursors to navigate collections for more information. 

    - include_entities
	When set to either true, t or 1, each tweet will include a node called 
    “entities”. This node offers a variety of metadata about the tweet in a 
    discrete structure, including: user_mentions, urls, and hashtags. While 
    entities are opt-in on timelines at present, they will be made a default 
    component of output in the future. See Tweet Entities for more details. 

	- skip_status
	When set to either true, t or 1 statuses will not be included in the 
    returned user objects.'''

    def __init__(self):
        super().__init__()
        self._method = get 

    def __call__(self, list_id=None, slug=None, owner_screen_name=None,
            owner_id=None, count=20, cursor=None, include_entities=False, 
            skip_status=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 list_id           -> int
 slug              -> string
 owner_screen_name -> string
 owner_id          -> int
 count             -> int <= 5000
 cursor            -> string
 include_entities  -> bool
 skip_status       -> bool'''

class members_endpoint(Collision): 
    '''Returns the members of the specified list. Private list members will only 
be shown if the authenticated user owns the specified list. 

	- list_id
	The numerical id of the list. 

	- slug
	You can identify a list by its slug instead of its numerical id. If you 
    decide to do so, note that you’ll also have to specify the list owner using 
    the owner_id or owner_screen_name parameters. 

	- owner_screen_name
	The screen name of the user who owns the list being requested by a slug. 

	- owner_id
	The user ID of the user who owns the list being requested by a slug. 

	- count
	Specifies the number of results to return per page (see cursor below). The 
    default is 20, with a maximum of 5,000. 

	- cursor
	Causes the collection of list members to be broken into “pages” of 
    consistent sizes (specified by the count parameter). If no cursor is 
    provided, a value of -1 will be assumed, which is the first “page.” The 
    response from the API will include a previous_cursor and next_cursor to 
    allow paging back and forth. See Using cursors to navigate collections for 
    more information. 

	- include_entities
	The entities node will be disincluded when set to false. 

	- skip_status
	When set to either true, t or 1 statuses will not be included in the 
    returned user objects.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, list_id=None, slug=None, owner_screen_name=None, 
            owner_id=None, count=20, cursor=None, include_entities=False, 
            skip_status=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 list_id           -> int
 slug              -> string
 owner_screen_name -> string
 owner_id          -> int
 count             -> int <= 5000
 cursor            -> string
 include_entities  -> bool
 skip_status       -> bool'''

class destroy(AbstractBase): 
    '''Deletes the specified list. The authenticated user must own the list to 
be able to destroy it. 

	- owner_screen_name
	The screen name of the user who owns the list being requested by a slug. 

	- owner_id
	The user ID of the user who owns the list being requested by a slug. 

	- list_id
	The numerical id of the list. 

	- slug
	You can identify a list by its slug instead of its numerical id. If you 
    decide to do so, note that you’ll also have to specify the list owner using 
    the owner_id or owner_screen_name parameters.'''

    def __init__(self):
        super().__init__()
        self._method = post 

    def __call__(self, owner_screen_name=None, owner_id=None, list_id=None, 
            slug=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 owner_screen_name -> string
 owner_id          -> int
 list_id           -> int
 slug              -> string'''

class update(AbstractBase): 
    '''Updates the specified list. The authenticated user must own the list to 
be able to update it. 

	- list_id
	The numerical id of the list. 

	- slug
	You can identify a list by its slug instead of its numerical id. If you 
    decide to do so, note that you’ll also have to specify the list owner using 
    the owner_id or owner_screen_name parameters. 

	- name
	The name for the list. 

	- mode
	Whether your list is public or private. Values can be public or private. If 
    no mode is specified the list will be public. 

	- description
	The description to give the list. 

	- owner_screen_name
	The screen name of the user who owns the list being requested by a slug. 

	- owner_id
	The user ID of the user who owns the list being requested by a slug.'''

    def __init__(self):
        super().__init__()
        self._method = post 

    def __call__(self, list_id=None, slug=None, name=None, mode=None, 
            description=None, owner_screen_name=None, owner_id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 list_id           -> int
 slug              -> string
 name              -> string
 mode              -> str in {'public', 'private'}
 description       -> string
 owner_screen_name -> string
 owner_id          -> int'''

class create(AbstractBase): 
    '''Creates a new list for the authenticated user. Note that you can create 
up to 1000 lists per account. 

	- name
	The name for the list. A list’s name must start with a letter and can 
    consist only of 25 or fewer letters, numbers, “-“, or “_” characters. 

	- mode
	Whether your list is public or private. Values can be public or private. If 
    no mode is specified the list will be public. 

	- description
	The description to give the list.'''

    def __init__(self):
        super().__init__()
        self._method = post 

    def __call__(self, name=None, mode=None, description=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 name        -> string
 mode        -> str in {'public', 'private'}
 description -> string'''

class show(AbstractBase): 
    '''Returns the specified list. Private lists will only be shown if the 
authenticated user owns the specified list. 

	- list_id
	The numerical id of the list. 

	- slug
	You can identify a list by its slug instead of its numerical id. If you 
    decide to do so, note that you’ll also have to specify the list owner using 
    the owner_id or owner_screen_name parameters. 

	- owner_screen_name
	The screen name of the user who owns the list being requested by a slug. 

	- owner_id
	The user ID of the user who owns the list being requested by a slug.'''

    def __init__(self):
        super().__init__()
        self._method = get 

    def __call__(self, list_id=None, slug=None, owner_screen_name=None, 
            owner_id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 list_id           -> int
 slug              -> string
 owner_screen_name -> string
 owner_id          -> int'''

class subscriptions(AbstractBase): 
    '''Obtain a collection of the lists the specified user is subscribed to, 20 
lists per page by default. Does not include the user’s own lists. 

	- user_id
	The ID of the user for whom to return results for. Helpful for 
    disambiguating when a valid user ID is also a valid screen name. 

	- screen_name
	The screen name of the user for whom to return results for. Helpful for 
    disambiguating when a valid screen name is also a user ID. 

	- count
	The amount of results to return per page. Defaults to 20. No more than 1000 
    results will ever be returned in a single page. 

	- cursor
	Breaks the results into pages. Provide a value of -1 to begin paging. 
    Provide values as returned in the response body’s next_cursor and 
    previous_cursor attributes to page back and forth in the list. It is 
    recommended to always use cursors when the method supports them. See 
    [node:10362] for more information.'''

    def __init__(self):
        super().__init__()
        self._method = get 

    def __call__(self, user_id=None, screen_name=None, count=20, cursor=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 user_id     -> int
 screen_name -> string
 count       -> int <= 1000
 cursor      -> string'''

class ownerships(AbstractBase): 
    '''Returns the lists owned by the specified Twitter user. Private lists will 
only be shown if the authenticated user is also the owner of the lists. 

	- user_id
	The ID of the user for whom to return results for. 

	- screen_name
	The screen name of the user for whom to return results for. 

	- count
	The amount of results to return per page. Defaults to 20. No more than 1000 
    results will ever be returned in a single page. 

	- cursor
	Breaks the results into pages. Provide a value of -1 to begin paging. 
    Provide values as returned in the response body’s next_cursor and 
    previous_cursor attributes to page back and forth in the list. It is 
    recommended to always use cursors when the method supports them. See 
    [node:10362] for more information.'''

    def __init__(self):
        super().__init__()
        self._method = get 

    def __call__(self, user_id=None, screen_name=None, count=20, cursor=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 user_id     -> int
 screen_name -> string
 count       -> int <= 1000
 cursor      -> string'''

# encapsulate namespace
lists = AbstractModule(globals())
setattr(lists, 'members', members)
setattr(lists, 'subscribers', subscribers)

# enforce singleton
del (List, statuses, memberships, subscribers_endpoint, members_endpoint, destroy, update, create,
     show, subscriptions, ownerships, members, subscribers,
     
     AbstractBase, AbstractModule, Collision, post, get)
