try:
    from twitter.application.api.superclass.abstract_base_class import AbstractBase
    from twitter.application.api.superclass.abstract_module import AbstractModule
    from twitter.application.api.superclass.superclasses import Ternary
    from twitter.application.api.superclass.superclasses import Numeric
    from twitter.application.subprocess.subroutines import filter
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_base_class import AbstractBase
    from application.api.superclass.abstract_module import AbstractModule
    from application.api.superclass.superclasses import Ternary
    from application.api.superclass.superclasses import Numeric
    from application.subprocess.subroutines import filter
finally:    
    from requests import get

class slug(Ternary): 
    '''Access the users in a given category of the Twitter suggested user list. 

It is recommended that applications cache this data for no more than one hour. 

	- slug
	The short name of list or a category 

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
        self._url = self.url.replace('slug.json', '{slug}.json')
        self._endpoint = self.endpoint.replace('slug', ':slug')

    def __call__(self, slug=None, lang=None):
        url = self.url
        self._url = self.url.format_map(vars())
        response = super().__call__(**{'lang': lang})
        self._url = url
        return response

    def __repr__(self):
        return '''PARAMETERS
 slug -> string
 lang -> two letter ISO 639-1 specification'''

class members(slug):
    '''Access the users in a given category of the Twitter suggested user list 
and return their most recent status if they are not a protected user. 

	- slug
	The short name of list or a category'''

    def __init__(self):
        super().__init__()
        self._method = get
        self._url = self.url.replace('.json', '/members.json')
        self._endpoint += '/members'

    def __call__(self, slug=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 slug -> string'''

suggestions = AbstractModule(globals())
