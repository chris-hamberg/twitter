try:    
    from twitter.application.api.superclass.abstract_module import AbstractModule
    from twitter.application.api.superclass.superclasses import Ternary
    from twitter.application.api._direct_messages.dm_template import dm
    from twitter.application.subprocess.subroutines import filter
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_module import AbstractModule
    from application.api.superclass.superclasses import Ternary
    from application.api._direct_messages.dm_template import dm
    from application.subprocess.subroutines import filter
finally:
    from requests import get, post, delete
    import json, copy

class new(Ternary):
    '''Publishes a new message_create event resulting in a Direct Message sent 
to a specified user from the authenticating user. Returns an event if 
successful. Supports publishing Direct Messages with optional Quick Reply and 
media attachment. Replaces behavior currently provided by POST 
direct_messages/new.

Requires a JSON POST body and Content-Type header to be set to application/json. 
Setting Content-Length may also be required if it is not automatically.
        
    - id 
    The ID of the user who should receive the direct message.

    - message
    The Message to deliver to the reciepient.'''

    def __init__(self):
        super().__init__()
        self._method = post
        self._headers.update({'content-type': 'application/json'})

    def __call__(self, id=None, text=None, media=None, opts=None, tweet_id=None,
            welcome_message_id=None): 
        msg = copy.deepcopy(dm)
        #NOTE not sure what is going on with these
        ##### whether these are user config opts
        ##### or always set by twitter. The docs are unclear
        msg['event']['initiated_via']['tweet_id'] = tweet_id
        msg['event']['initiated_via']['welcome_message_id'] = welcome_message_id
        ##########################################
        msg['event']['message_create']['target']['recipient_id'] = id
        msg['event']['message_create']['message_data']['text'] = text
        msg['event']['message_create']['quick_reply_response']['options'] = opts
        msg['event']['message_create']['attachment']['media'] = media
        self._data = json.dumps(msg)
        return super().__call__()

    def __repr__(self):
        return '''PARAMETERS
 id             -> int; user id
 message        -> string
 custom_profile -> int; custom profile id'''

class show(Ternary):
    '''Returns a single direct message, specified by an id parameter. Like the 
/1.1/direct_messages.format request, this method will include the user objects 
of the sender and recipient. 

Important: This method requires an access token with RWD (read, write & direct 
message) permissions. Consult The Application Permission Model for more 
information. 

	- id
	The ID of the direct message.'''
   
    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 id -> int; msg id'''

class List(Ternary):
    '''Returns all Direct Message events (both sent and received) within the 
last 30 days. Sorted in reverse-chronological order.
        
    - count 
    Max number of events to be returned. 20 default. 50 max.

    - cursor 
    For paging through result sets greater than 1 page, use the “next_cursor” 
    property from the previous request.'''

    def __init__(self):
        super().__init__()
        self._method = get

    def __call__(self, count=20, cursor=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 count  -> int <= 50
 cursor -> int'''

class destroy(Ternary):
    '''Deletes the direct message specified in the required ID parameter. The 
authenticating user must be the recipient of the specified direct message. 
Direct Messages are only removed from the interface of the user context 
provided. Other members of the conversation can still access the Direct 
Messages. A successful delete will return a 204 http response code with no body 
content.

Important: This method requires an access token with RWD (read, write & direct 
message) permissions.

    - id 
    The id of the Direct Message event that should be deleted.'''

    def __init__(self):
        super().__init__()
        self._method = delete

    def __call__(self, id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 id -> int; msg id'''

# encapsulate namespace
events = AbstractModule(globals())

# enforce singleton
del (show, new, List, destroy,
     AbstractModule, Ternary, get, post, delete)
