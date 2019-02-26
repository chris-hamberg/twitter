try:
    from twitter.application.api.superclass.abstract_base_class import AbstractBase
    from twitter.application.api.superclass.abstract_module import AbstractModule
    from twitter.application.extras.exceptions import CacheError 
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_base_class import AbstractBase
    from application.api.superclass.abstract_module import AbstractModule
    from application.extras.exceptions import CacheError 
finally:
    from requests import get

class rate_limit_status(AbstractBase):
    '''Returns the current rate limits for methods belonging to the specified 
resource families. 

Each 1.1 API resource belongs to a “resource family” which is indicated in its 
method documentation. You can typically determine a method’s resource family 
from the first component of the path after the resource version. 

This method responds with a map of methods belonging to the families specified 
by the resources parameter, the current remaining uses for each of those 
resources within the current rate limiting window, and its expiration time in 
epoch time. It also includes a rate_limit_context field that indicates the 
current access token or application-only authentication context. 

You may also issue requests to this method without any parameters to receive a 
map of all rate limited GET methods. If your application only uses a few of 
methods, please explicitly provide a resources parameter with the specified 
resource families you work with. 

When using app-only auth, this method’s response indicates the app-only auth 
rate limiting context. 

Read more about API Rate Limiting and review the limits. 

    - resources
    A comma-separated list of resource families you want to know the current 
    rate limit disposition for. For best performance, only specify the resource 
    families pertinent to your application. See API Rate Limiting for more 
    information.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, resources=None):

        if self.twitter.CACHE_LOCKED: 
            # caching is off or we are updating the cache
            return super().__call__()

        elif not bool(self.twitter.cache) or self.twitter.cache.expired:
            # the cache does not exist or the cache is expired
            # create a new cache
            try:
                self.twitter.cache.refresh(self)
            except CacheError as a_problem:
                self.twitter.log.debug(a_problem)
        
        try:
            return self.twitter.cache[resources]
        except KeyError as update:
            return self.twitter.cache

    def __repr__(self):
        return ''' PARAMETERS
 resources -> a comma-seperated list of resource families'''

# encapsulate namespace
application = AbstractModule(globals())

# enforce singleton
del rate_limit_status, AbstractBase, AbstractModule, get
