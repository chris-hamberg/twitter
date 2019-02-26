def evaluate(twitter, module):

    ######################################
    ''' Each end point is tested here. '''
    ######################################
    fail = False
    #TODO the test!
    for endpoint in module:
        try:
            endpoint.response.raise_for_status()
        except Exception: # the response failed :(
            fail = True
            twitter.log.error('[FAIL]: {endpoint.parent}.'
            '{endpoint.__class__.__name__} '.format_map(vars(
                        )))
    return fail # returns True if at least one failure occured.
