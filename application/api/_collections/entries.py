try:
    from twitter.application.api.superclass.abstract_module import AbstractModule
    from twitter.application.api.superclass.superclasses import Ternary
    from twitter.application.subprocess.subroutines import filter
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_module import AbstractModule
    from application.api.superclass.superclasses import Ternary
    from application.subprocess.subroutines import filter
finally:
    from requests import delete, post, get
    import json

class add(Ternary):
    '''Add a specified Tweet to a Collection.

A collection will store up to a few thousand Tweets. Adding a Tweet to a 
collection beyond its allowed capacity will remove the oldest Tweet in the 
collection based on the time it was added to the collection.

Use POST collections / entries / curate to add Tweets to a Collection in bulk.

    - id
    The identifier of the Collection receiving the Tweet.

    - tweet_id
    The identifier of the Tweet to add to the Collection.

    - relative_to
    The identifier of the Tweet used for relative positioning in a 
    curation_reverse_chron ordered collection.

    - above
    Set to false to insert the specified tweet_id below the relative_to Tweet 
    in the collection.'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, id=None, tweet_id=None, relative_to=None, above=True):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 id          -> string
 tweet_id    -> int
 relative_to -> int; tweet id
 above       -> bool'''

class curate(Ternary):
    '''Curate a Collection by adding or removing Tweets in bulk. Updates must be 
limited to 100 cumulative additions or removals per request.

Use POST collections / entries / add and POST collections / entries / remove to 
add or remove a single Tweet.'''

    def __init__(self):
        super().__init__()
        self._method = post
        self._headers.update({'content-type': 'application/json'})

    def __call__(self, id, tweet_ids):
        #NOTE this is extremely bad practice forced by Twitter.
        ##### These json structures should be sitting behind
        ##### the server interface. It is neither user friendly
        ##### nor is it efficent, since it maximizes the size 
        ##### of n (that is, the size of the problem) at the 
        ##### bottle neck of even the most efficient client.
        self._data = json.dumps({"id": id, "changes": [
            {"op": "add", "tweet_id": tweet_id
            } for tweet_id in tweet_ids
            ]})
        return super().__call__()

    def __repr__(self):
        return '''PARAMETERS
 id -> string; collection ID
 tweet_ids -> Python sequence of tweet ids (tuple, list, or set)'''

class move(Ternary):
    '''Move a specified Tweet to a new position in a curation_reverse_chron 
ordered collection.

    - id
    The identifier of the Collection receiving the Tweet.
    
    - tweet_id
    The identifier of the Tweet to add to the Collection.

    - relative_to
    The identifier of the Tweet used for relative positioning.

    - above
    Set to false to insert the specified tweet_id below the relative_to Tweet in 
    the collection.'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, id=None, tweet_id=None, relative_to=None, above=True):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 id          -> string
 tweet_id    -> int
 relative_to -> int; tweet_id
 above       -> bool'''

class remove(Ternary):
    '''Remove the specified Tweet from a Collection.

Use POST collections / entries / curate to remove Tweets from a Collection in 
bulk.

    - id
    The identifier of the target Collection.

    - tweet_id
    The identifier of the Tweet to remove.'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, id=None, tweet_id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 id       -> string
 tweet_id -> int'''

# encapsulate namespace
entries = AbstractModule(globals())

# enforce singleton
del (add, curate, move, remove,
     AbstractModule, Ternary, delete, post, get)

