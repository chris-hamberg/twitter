try:
    from twitter.application.extras.containers import RateLimitedResponse
    from twitter.application.extras.exceptions import NotAuthorizedError
    from twitter.application.extras.containers import ErrorResponse
    from twitter.application.extras.containers import MockResponse
except ModuleNotFoundError as main:
    from application.extras.containers import RateLimitedResponse
    from application.extras.exceptions import NotAuthorizedError
    from application.extras.containers import ErrorResponse
    from application.extras.containers import MockResponse
finally:
    from requests.exceptions import ConnectionError, HTTPError

MESSAGE  = '{response.status_code}: {url}: limit: {remaining}'

def requests(api):

    #######################################################
    '''        A not so cliche requests wrapper.        '''
    #######################################################

    Response = None

    try:
        if not twitter.mock:
            assert twitter.auth
    except AssertionError as no_oauth_token:
        raise NotAuthorizedError (twitter.username)

    ### Get rate limit from cache; (unless already getting)
    remaining = float('inf') if (twitter.CACHE_LOCKED
            ) else twitter.cache.query(api)
    #######################################################

    try:

        if twitter.mock: ### we are just doing a test.
            response = MockResponse(api.url)
        
        else: #TODO the real request.
    
            True/remaining #NOTE division by zero means rate limited
        
            response = api.method(url     = api.url,
                                  params  = api.params,
                                  data    = api.data,
                                  headers = api.headers,
                                  auth    = twitter.auth
                                  )
            
            ################ update the cache #################
            remaining -= 1
            if not twitter.CACHE_LOCKED: twitter.cache.set(api)            
            ###################################################
            
            response.raise_for_status() # check for server error
            
    except (ConnectionError, HTTPError) as server_error:
        twitter.log.error(server_error.response or server_error)
        return ErrorResponse(api.url, server_error)
    except (ZeroDivisionError, TypeError):
        twitter.log.error('RATE LIMIT REACHED')
        return RateLimitedResponse(api.url) # NOTE polymorphic DataCapsule
    else: 
        # The response succeeded
        url = response.url[28:].split('.')[0]
        twitter.log.info(MESSAGE.format_map(vars()))
        return response
