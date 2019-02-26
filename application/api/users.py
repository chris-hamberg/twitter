try:
    from twitter.application.api.superclass.abstract_base_class import AbstractBase
    from twitter.application.api.superclass.abstract_module import AbstractModule
    from twitter.application.api.superclass.superclasses import Collision
    from twitter.application.api._users.suggestions import suggestions
    from twitter.application.subprocess.subroutines import filter
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_base_class import AbstractBase
    from application.api.superclass.abstract_module import AbstractModule
    from application.api.superclass.superclasses import Collision
    from application.api._users.suggestions import suggestions
    from application.subprocess.subroutines import filter
finally:    
    from requests import post, get

class lookup(AbstractBase): 
    '''Returns fully-hydrated user objects for up to 100 users per request, as 
specified by comma-separated values passed to the user_id and/or screen_name 
parameters. 

This method is especially useful when used in conjunction with collections of 
user IDs returned from GET friends / ids and GET followers / ids. 

GET users / show is used to retrieve a single user object. 


There are a few things to note when using this method. 

		You must be following a protected user to be able to see their most 
        recent status update. If you don’t follow a protected user their status 
        will be removed. 

		The order of user IDs or screen names may not match the order of users 
        in the returned array. 

		If a requested user is unknown, suspended, or deleted, then that user 
        will not be returned in the results list. 

		If none of your lookup criteria can be satisfied by returning a user 
        object, a HTTP 404 will be thrown. 

		You are strongly encouraged to use a POST for larger requests. 

	- screen_name
	A comma separated list of screen names, up to 100 are allowed in a single 
    request. You are strongly encouraged to use a POST for larger (up to 100 
    screen names) requests. 

	- user_id
	A comma separated list of user IDs, up to 100 are allowed in a single 
    request. You are strongly encouraged to use a POST for larger requests. 

	- include_entities
	The entities node that may appear within embedded statuses will be 
    disincluded when set to false.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, screen_name=None, user_id=None, include_entities=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 screen_name      -> comma separated list of strings
 user_id          -> comma separated list of ints
 include_entities -> bool'''

class show(AbstractBase): 
    '''Returns a variety of information about the user specified by the required 
user_id or screen_name parameter. The author’s most recent Tweet will be 
returned inline when possible. 

GET users / lookup is used to retrieve a bulk collection of user objects. 

You must be following a protected user to be able to see their most recent 
Tweet. If you don’t follow a protected user, the users Tweet will be removed. A 
Tweet will not always be returned in the current_status field. 

	- user_id
	The ID of the user for whom to return results for. Either an id or 
    screen_name is required for this method. 

	- screen_name
	The screen name of the user for whom to return results for. Either a id or 
    screen_name is required for this method. 

	- include_entities
	The entities node will be disincluded when set to false.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, user_id=None, screen_name=None, include_entities=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 user_id          -> int
 screen_name      -> string
 include_entities -> bool'''

class search(AbstractBase): 
    '''Provides a simple, relevance-based search interface to public user 
accounts on Twitter. Try querying by topical interest, full name, company name, 
location, or other criteria. Exact match searches are not supported. 

Only the first 1,000 matching results are available. 

	- q
	The search query to run against people search. 

	- page
	Specifies the page of results to retrieve. 

	- count
	The number of potential user results to retrieve per page. This value has a 
    maximum of 20. 

	- include_entities
	The entities node will be disincluded from embedded tweet objects when set 
    to false.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, q=None, page=None, count=20, include_entities=False):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 q                -> query string
 page             -> int
 count            -> int <= 20
 include_entities -> bool'''

class profile_banner(AbstractBase): 
    '''Returns a map of the available size variations of the specified user’s 
profile banner. If the user has not uploaded a profile banner, a HTTP 404 will 
be served instead. This method can be used instead of string manipulation on the 
profile_banner_url returned in user objects as described in Profile Images and 
Banners. 

The profile banner data available at each size variant’s URL is in PNG format. 

	- user_id
	The ID of the user for whom to return results. Helpful for disambiguating 
    when a valid user ID is also a valid screen name. 

	- screen_name
	The screen name of the user for whom to return results. Helpful for 
    disambiguating when a valid screen name is also a user ID.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, user_id=None, screen_name=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 user_id     -> int
 screen_name -> string'''

class suggestions_endpoint(Collision): 
    '''Access to Twitter’s suggested user list. This returns the list of 
suggested user categories. The category can be used in GET users / suggestions / 
:slug to get the users in that category. 

	- lang
	Restricts the suggested categories to the requested language. The language 
    must be specified by the appropriate two letter ISO 639-1 representation. 
    Currently supported languages are provided by the GET help / languages API 
    request. Unsupported language codes will receive English (en) results. If 
    you use lang in this request, ensure you also include it when requesting the 
    GET users / suggestions / :slug list.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, lang=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 lang -> two letter ISO 639-1 specification'''

class report_spam(AbstractBase): 
    '''Report the specified user as a spam account to Twitter. Additionally 
performs the equivalent of POST blocks / create on behalf of the authenticated 
user. 

	- screen_name
	The ID or screen_name of the user you want to report as a spammer. Helpful 
    for disambiguating when a valid screen name is also a user ID. 

	- user_id
	The ID of the user you want to report as a spammer. Helpful for 
    disambiguating when a valid user ID is also a valid screen name.'''

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

# encapsulate namespace
users = AbstractModule(globals())
setattr(users, 'suggestions', suggestions)

# enforce singleton
del (lookup, show, search, profile_banner, suggestions_endpoint, report_spam,
        
     AbstractBase, AbstractModule, Collision, suggestions, post, get)
