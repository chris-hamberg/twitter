''' A module of special exceptions '''
# NOTE Although we only have two now...
# this is its own separate module in
# case of future requirements updates

class CacheError(Exception): pass

class NotAuthorizedError(Exception): pass
