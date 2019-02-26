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
    '''Subscribes the authenticated user to the specified list. 

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

class show(Ternary):
    '''Check if the specified user is a subscriber of the specified list. 
Returns the user if they are subscriber. 

	- owner_screen_name
	The screen name of the user who owns the list being requested by a slug. 

	- owner_id
	The user ID of the user who owns the list being requested by a slug. 

	- list_id
	The numerical id of the list. 

	- slug
	You can identify a list by its slug instead of its numerical id. If you 
    decide to do so, note that you’ll also have to specify the list owner using 
    the owner_id or owner_screen_name parameters. 

	- user_id
	The ID of the user for whom to return results for. Helpful for 
    disambiguating when a valid user ID is also a valid screen name. 

	- screen_name
	The screen name of the user for whom to return results for. Helpful for 
    disambiguating when a valid screen name is also a user ID. 

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

    def __call__(self, owner_screen_name=None, owner_id=None, list_id=None, 
            slug=None, user_id=None, screen_name=None, include_entities=False, 
            skip_status=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 owner_screen_name -> string
 owner_id          -> int
 list_id           -> int
 slug              -> string
 user_id           -> int
 screen_name       -> string
 include_entities  -> bool
 skip_status       -> bool'''

class destroy(Ternary): 
    '''Unsubscribes the authenticated user from the specified list. 

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
        self._method = post

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

# encapsulate namespace
subscribers = AbstractModule(globals())

# enforce singleton
del (create, destroy, show,
     Ternary, AbstractModule, post, get)
