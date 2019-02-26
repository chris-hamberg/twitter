#NOTE used by the connection module request function requests wrapper

class DataContainer:

    def __init__(self, url, payload=None):
        self._url = url
        self._json = payload
    
    def json(self):
        return self._json

    def __repr__(self): raise NotImplementedError

    @property
    def url(self):
        return self._url

class RateLimitedResponse(DataContainer):

    def __init__(self, url):
        super().__init__(url)
        
    def raise_for_status(self):
        return 'RATE LIMITED'
    
    def __repr__(self):
        return '<RateLimitedResponse [429]>'

    @property
    def status_code(self):
        return 429

class MockResponse(DataContainer):

    def __init__(self, url):
        super().__init__(url)
        self._json = {"resources": {"statuses": 
            {"/statuses/home_timeline": {"remaining":0}
                }}}

    def raise_for_status(self):
        return self.status_code

    def __repr__(self):
        return '<MockResponse [200]>'

    @property
    def status_code(self):
        return 200

class ErrorResponse(DataContainer):

    def __init__(self, url, error):
        super().__init__(url)
        self._error = error
    
    def raise_for_status(self):
        raise self._error

    def __repr__(self):
        return '<ErrorResponse [400 - 500]>'

    def status_code(self):
        return 'unknown'
