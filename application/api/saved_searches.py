try:
    from twitter.application.api.superclass.abstract_base_class import AbstractBase
    from twitter.application.api.superclass.abstract_module import AbstractModule
    from twitter.application.api.superclass.superclasses import Numeric
    from twitter.application.api.superclass.superclasses import Empty
    from twitter.application.subprocess.subroutines import filter
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_base_class import AbstractBase
    from application.api.superclass.abstract_module import AbstractModule
    from application.api.superclass.superclasses import Numeric
    from application.api.superclass.superclasses import Empty
    from application.subprocess.subroutines import filter
finally:    
    from requests import post, get

class List(Empty): 
    '''Returns the authenticated user’s saved search queries.'''
    
    def __init__(self):
        super().__init__()
        self._method = get

class show(Numeric): 
    '''Retrieve the information for the saved search represented by the given 
id. The authenticating user must be the owner of saved search ID being 
requested. 

	- id
	The ID of the saved search.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 id -> int'''

class create(AbstractBase): 
    '''Create a new saved search for the authenticated user. A user may only 
have 25 saved searches. 

	- query
	The query of the search the user would like to save. The query must be 100 
    characters or less.'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, query=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 query -> len(string) <= 100'''

class destroy(Numeric): 
    '''Destroys a saved search for the authenticating user. The authenticating 
user must be the owner of saved search id being destroyed. 

	- id
	The ID of the saved search.'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 id -> int'''

# encapsulate namespace
saved_searches = AbstractModule(globals())

# enforce singleton
del (List, create, destroy, show,
     Numeric, Empty, AbstractBase, AbstractModule, post, get)
