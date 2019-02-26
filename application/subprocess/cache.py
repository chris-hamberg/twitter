try:
    from twitter.application.subprocess.subroutines import exponential_backoff
    from twitter.application.extras.exceptions import CacheError
except ModuleNotFoundError as main:
    from application.subprocess.subroutines import exponential_backoff
    from application.extras.exceptions import CacheError
finally:    
    import datetime, time

EXPIRATION = 15

class RateLimitCache(dict):

    DELTA = datetime.timedelta(minutes=EXPIRATION)

    def __init__(self):
        self._epoch = None
        self._expiration = None

    def query(self, api, remaining=None):
        try:
            self.refresh(api) if self.expired else True
            parent    = self.get(api.parent)
            endpoint  = parent.get(api.endpoint)
            remaining = endpoint.get('remaining')
        except AttributeError as missing_dictionary:
            self.twitter.log.debug(missing_dictionary)
        except CacheError as fatal_exception:
            self.post_mortem(api, fatal_exception)
        finally:
            # TODO This is a problem if remaining is zero
            return remaining or float('inf')

    def set(self, api):
        try:
            self[api.parent][api.endpoint]['remaining'] -= 1
        except (KeyError, AttributeError, TypeError) as not_rate_limited:
            pass

    def refresh(self, api):
        for attempt in exponential_backoff(api):
            try:
                self.refresh_handler(api)
            except AttributeError as bad_response:
                'back off'
            else:
                self.release(api)
                return 0
        raise CacheError('caching diabled')

    def release(self, api):
        self.twitter.CACHE_LOCKED = False
        self._set_expiration()

    def refresh_handler(self, api):
        self.twitter.CACHE_LOCKED = True
        response = self.twitter.application.rate_limit_status()
        self.twitter.cache.update(response.json()['resources'])

    def post_mortem(self, api, fatal_exception):
        self.twitter.CACHE_LOCKED = True
        self.twitter.log.critical(
                'CacheError: {fatal_exception}'.format_map(vars(
                    )))

    def _set_expiration(self):
        self.epoch = datetime.datetime.utcnow()
        self.expiration = self.epoch + RateLimitCache.DELTA

    @property
    def epoch(self):
        return self._epoch

    @epoch.setter
    def epoch(self, time):
        self._epoch = time

    @property
    def expiration(self):
        return self._expiration

    @expiration.setter
    def expiration(self, time):
        self._expiration = time
    
    @property
    def expired(self):
        try:
            return datetime.datetime.utcnow() >= self.expiration
        except TypeError as cache_doesnt_exist:
            return True
