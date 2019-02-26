try:
    from twitter.application.api.superclass.abstract_base_class import AbstractBase
    from twitter.application.subprocess.base64encode import base64encode
    from twitter.application.subprocess.connection import requests
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_base_class import AbstractBase
    from application.subprocess.base64encode import base64encode
    from application.subprocess.connection import requests
finally:
    from requests import get, post
    import inspect

# ----------------------------------------------------------------------- #
'''
Special classes for handling edge cases, as the occur in the api definition 
'''
# ---------------------------------------=------------------------------- #

class Base64(AbstractBase):
    '''
    update_profile_image, and update_profile_banner classes inherit from 
    this class.
    '''
    def __init__(self):
        super().__init__()
        self._method = post
        self._endpoint = None
        self._key = None

    #NOTE do the base64 encoding procedure !!!
    def __call__(self, **params):
        self._data = base64encode(params)
        try:
            # NOTE direct_messages changed state
            ###### by adding the content-type
            ###### field to headers.
            ###### try to pop content-type.
            self._headers.pop('content-type')
        except KeyError as good:
            pass
        return AbstractBase.__call__(self, **params)

    def __repr__(self): raise NotImplementedError

class Collision(AbstractBase):
    '''
    For some reason the API was written to have name collisions.
    
    collections/entires had to ve renamed to collections/entries_method
    list/members had to be renamed to list/members_method

    this superclass corrects the urls and endpoints for these classes
    '''
    def __init__(self):
        super().__init__()
        surrogate  = self.__class__.__name__
        biological = surrogate.split('_')[0]
        self._url  = self.url.replace(surrogate, biological)
        self._endpoint = self._endpoint.split('_')[0]

    def __repr__(self): raise NotImplementedError

class Empty(AbstractBase):
    '''
    settings, and remove_profile_banner classes inherit from this class.
    '''
    def __init__(self):
        super().__init__()
        del self._params, self._data

    def __call__(self): #NOTE neither of these subclasses take any arg
        return AbstractBase.__call__(self)

    def __repr__(self):
        return ' PARAMETERS: None'

class Media(AbstractBase):

    def __init__(self):
        super().__init__()
        self._method = post
        self._url = self.url.replace('api', 'upload')
        self._url = self.url.replace(self.__class__.__name__.lower(), 
                'upload')
        self._endpoint = self.endpoint.replace(self.__class__.__name__.lower(), 
                'upload')
        try:
            self._headers.pop('content-type')
        except KeyError as good: pass

    def __call__(self, **params):
        if self.__class__.__name__ != 'upload':
            params.update({'command': self.__class__.__name__})
        return AbstractBase.__call__(self, **params)

    def __repr__(self): raise NotImplementedError

class Numeric(AbstractBase):
    ''' 
    retweets, retweet, and unretweet classes inherit from this class.
    All other status module classes are children of AbstractBase.
    '''
    def __init__(self, suffix=None):
        # because the retweets class is a special edge case; where
        # str.rstrip('.json') removes the trailing 's' from 'retweets',
        # we need the following conditional statement to handle that 
        # deformation.
        if not suffix: 
            suffix = '/{id}.json'
        super().__init__()
        self._method = post
        self._url    = self._url.rstrip('.json') + suffix

    def __call__(self, **params): #NOTE these endpoints are of a special form.
        url = self.url
        self._url = self.url.format_map(params)
        response = AbstractBase.__call__(self, **params)
        self._url = url
        return response
    
    def __repr__(self): raise NotImplementedError

class Ternary(AbstractBase):

    def __init__(self):
        self._method = None
        super().__init__()

        frame = inspect.currentframe()
        fpath = inspect.getouterframes(frame, 2)[9][1]
        module = fpath.split('/')[-1].split('.')[0]

        self._module = module

        url = self.url.split('/')
        url.insert(-2, self.parent)
        url = '/'.join(url)
        self._url = url

        self._endpoint = '/'+self.parent+self._endpoint

    def __repr__(self): raise NotImplementedError
