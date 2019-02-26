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

class destroy(Ternary): 
    '''Removes the specified member from the list. The authenticated user must 
be the list’s owner to remove members from the list. 

	- list_id
	The numerical id of the list. 

	- slug
	You can identify a list by its slug instead of its numerical id. If you 
    decide to do so, note that you’ll also have to specify the list owner using 
    the owner_id or owner_screen_name parameters. 

	- user_id
	The ID of the user to remove from the list. Helpful for disambiguating when 
    a valid user ID is also a valid screen name. 

	- screen_name
	The screen name of the user for whom to remove from the list. Helpful for 
    disambiguating when a valid screen name is also a user ID. 

	- owner_screen_name
	The screen name of the user who owns the list being requested by a slug. 

	- owner_id
	The user ID of the user who owns the list being requested by a slug.'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, list_id=None, slug=None, user_id=None, screen_name=None, 
            owner_screen_name=None, owner_id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 list_id           -> int
 slug              -> string
 user_id           -> int
 screen_name       -> string
 owner_screen_name -> string
 owner_id          -> int'''

class create_all(Ternary): 
    '''Adds multiple members to a list, by specifying a comma-separated list of
member ids or screen names. The authenticated user must own the list to be able 
to add members to it. Note that lists can’t have more than 5,000 members, and 
you are limited to adding up to 100 members to a list at a time with this 
method. 

Please note that there can be issues with lists that rapidly remove and add 
memberships. Take care when using these methods such that you are not too 
rapidly switching between removals and adds on the same list. 

	- list_id
	The numerical id of the list. 

	- slug
	You can identify a list by its slug instead of its numerical id. If you 
    decide to do so, note that you’ll also have to specify the list owner using 
    the owner_id or owner_screen_name parameters. 

	- user_id
	A comma separated list of user IDs, up to 100 are allowed in a single 
    request. 

	- screen_name
	A comma separated list of screen names, up to 100 are allowed in a single 
    request. 

	- owner_screen_name
	The screen name of the user who owns the list being requested by a slug. 

	- owner_id
	The user ID of the user who owns the list being requested by a slug.'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, list_id=None, slug=None, user_id=None, screen_name=None, 
            owner_screen_name=None, owner_id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 list_id           -> int
 slug              -> string
 user_id           -> int
 screen_name       -> string
 owner_screen_name -> string
 owner_id          -> int'''

class show(Ternary): 
    '''Check if the specified user is a member of the specified list. 

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

	- owner_screen_name
	The screen name of the user who owns the list being requested by a slug. 

	- owner_id
	The user ID of the user who owns the list being requested by a slug.

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

    def __call__(self, list_id=None, slug=None, user_id=None, screen_name=None, 
            owner_screen_name=None, owner_id=None, include_entities=False, 
            skip_status=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 list_id           -> int
 slug              -> string
 user_id           -> int
 screen_name       -> string
 owner_screen_name -> string
 owner_id          -> int
 include_entities  -> bool
 skip_status       -> bool'''

class create(Ternary): 
    '''Add a member to a list. The authenticated user must own the list to be 
able to add members to it. Note that lists cannot have more than 5,000 members. 

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

	- owner_screen_name
	The screen name of the user who owns the list being requested by a slug. 

	- owner_id
	The user ID of the user who owns the list being requested by a slug.'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, list_id=None, slug=None, user_id=None, screen_name=None, 
            owner_screen_name=None, owner_id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 list_id           -> int
 slug              -> string
 user_id           -> int
 screen_name       -> string
 owner_screen_name -> string
 owner_id          -> int'''

class destroy_all(Ternary): 
    '''Removes multiple members from a list, by specifying a comma-separated 
list of member ids or screen names. The authenticated user must own the list to 
be able to remove members from it. Note that lists can’t have more than 500 
members, and you are limited to removing up to 100 members to a list at a time 
with this method. 

Please note that there can be issues with lists that rapidly remove and add 
memberships. Take care when using these methods such that you are not too 
rapidly switching between removals and adds on the same list. 

	- list_id
	The numerical id of the list. 

	- slug
	You can identify a list by its slug instead of its numerical id. If you 
    decide to do so, note that you’ll also have to specify the list owner using 
    the owner_id or owner_screen_name parameters. 

	- user_id
	A comma separated list of user IDs, up to 100 are allowed in a single 
    request. 

	- screen_name
	A comma separated list of screen names, up to 100 are allowed in a single 
    request. 

	- owner_screen_name
	The screen name of the user who owns the list being requested by a slug. 

	- owner_id
	The user ID of the user who owns the list being requested by a slug.'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, list_id=None, slug=None, user_id=None, screen_name=None, 
            owner_screen_name=None, owner_id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 list_id           -> int
 slug              -> string
 user_id           -> int
 screen_name       -> string
 owner_screen_name -> string
 owner_id          -> int'''

# encapsulate namespace
members = AbstractModule(globals())

# enforce singleton
del (destroy, create_all, show, create, destroy_all,
    
     Ternary, AbstractModule, post, get)
