try:
    from twitter.application.subprocess.connection import requests
except ModuleNotFoundError as main:
    from application.subprocess.connection import requests
finally:
    import abc

class AbstractBase(abc.ABC):
    
    ###########################################
    # Every API Endpoint Inherits from ME !!! #
    ###########################################

    #NOTE
    '''
    Ultimately this class represents a url, and...
    
    ...if a request has been made to that url, then this class also stores the 
    response in RAM (the most recent response only).
    '''

    ################ Template URL and User-Agent ################
    BASE_URL = 'https://api.twitter.com/1.1/{self.endpoint}.json'
    HEADERS  = {'user-agent': 'Chrome/24.0.1312.27',
                'content-type': 'application/json'
               }
    #############################################################

    def __new__(cls):

        '# --------------------- #'
        '''      Singleton      '''
        '# --------------------- #'
        
        if not hasattr(cls, 'instance'):
            cls.instance = super(AbstractBase, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        '''
        Contruct the full url starting with the end point.

        __call__ connection to Twitter servers, for all endpoints.

        self.url and self.endpoint are read only, they also persist during 
        runtime as an optimization. This way the url need not be constructed 
        each time a request is made.
        '''
        self._module = self.__module__.split('.')[-1]
        self._endpoint = '/'.join([
                self._module.lower(), 
                self.__class__.__name__.lower()
                ])
        self._url = __class__.BASE_URL.format_map(vars())
        self._endpoint = '/' + self._endpoint
        self._headers = __class__.HEADERS
        self._params = None
        self._data   = None
        self._response = None

    def __call__(self, **params):
        '''
        A gateway for all out going requests (most of them)
        '''
        self._params = params
        self._response = requests(self)
        self._params, self._data = None, None
        return self.response
        
    #def __repr__(self): raise NotImplementedError()
    
    @property
    def url(self):
        return self._url

    @property
    def parent(self): #NOTE /statuses/update, statuses is the parent
        return self._module

    @property
    def endpoint(self): #NOTE /statuses/update is the endpoint
        return self._endpoint

    @property
    def headers(self):
        return self._headers

    @property
    def method(self): #NOTE http GET or POST method
        return self._method

    @property
    def params(self): ### as specified by the requests library
        try:
            return self._params
        except AttributeError:
            return dict()

    @property
    def data(self): ### as specified by the requests library
        try:
            return self._data
        except AttributeError:
            return str()

    @property ### keep most recent response (for particular endpoints)
    def response(self):
        return self._response
