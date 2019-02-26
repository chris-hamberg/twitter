from application.api.superclass.abstract_base_class import AbstractBase
from application.api.superclass.abstract_module import AbstractModule
from application.api.superclass.superclasses import Ternary
from application.subprocess.subroutines import filter
from application.api._direct_messages.rules import rules
from requests import delete, post, get, put
import json

class destroy(Ternary):

    def __init__(self):
        '''Deletes a Welcome Message by the given id.

    - id
    The id of the Welcome Message that should be deleted.'''
        super().__init__()
        self._method = delete

    def __call__(self, id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 id -> int'''

class show(Ternary):

    def __init__(self):
        '''Returns a Welcome Message by the given id.

    - id
    The id of the Welcome Message that should be returned.'''
        super().__init__()
        self._method = get

    def __call__(self, id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 id -> msg id'''

class new(Ternary):

    def __init__(self):
        '''Creates a new Welcome Message that will be stored and sent in the 
future from the authenticating user in defined circumstances. Returns the 
message template if successful. Supports publishing with the same elements as 
Direct Messages (e.g. Quick Replies, media attachments).

Requires a JSON POST body and Content-Type header to be set to application/json. 
Setting Content-Length may also be required if it is not automatically.

See the Welcome Messages overview to learn how to work with Welcome Messages.

    - message
    The Message Data content of the message.
    
    - name
    A human readable name for the Welcome Message. This is not displayed to the 
    user. Max length of 100 alpha numeric characters including hyphens, 
    underscores, spaces, hashes and at signs.

    - media
    Media attached to the message, by its media id.

        '''
        super().__init__()
        self._method = post
        self._headers.update({'content-type': 'application/json'})

    def __call__(self, message=None, name=None, media=None):
        welcome_message = {"welcome_message": {
                           "message_data"   : {"text": message
                               }}}
        if name:
            welcome_message['welcome_message'].update({"name": name})
        if id:
            welcome_message['welcome_message']['message_data'].update(
                    {"attachment": {
                        "type" : "media",
                        "media": {"id": media
                            }}})
        self._data = json.dumps(welcome_message)
        return super().__call__()

    def __repr__(self):
        return '''PARAMETERS 
 message -> string
 name    -> string
 media   -> media id'''

class list(Ternary):

    def __init__(self):
        '''Returns a list of Welcome Messages.
    
    - count
    Number of welcome messages to be returned. Max of 50. Default is 20.
    
    - cursor
    For paging through result sets greater than 1 page, use the “next_cursor” 
    property from the previous request.'''
        super().__init__()
        self._method = get

    def __call__(self, count=20, cursor=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 count  -> int
 cursor -> int'''

class update(Ternary):

    def __init__(self):
        '''Updates a Welcome Message by the given ID. Updates to the 
welcome_message object are atomic. For example, if the Welcome Message currently 
has quick_reply defined and you only provide text, the quick_reply object will 
be removed from the Welcome Message.
        
    - id
    The id of the Welcome Message that should be updated.'''
        super().__init__()
        self._method = put

    def __call__(self, id=None):
        return 'Not Implemented'
        #TODO return super().__call__(**filter(**vars(
        #    )))

    def __repr__(self):
        return '''PARAMETERS
        '''

welcome_messages = AbstractModule(globals())
setattr(welcome_messages, 'rules', rules)

del (destroy, show, new, list, update,
     AbstractBase, AbstractModule, Ternary, 
     delete, post, get, put, rules)
