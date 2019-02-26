try:
    from twitter.application.api.superclass.abstract_base_class import AbstractBase
    from twitter.application.api.superclass.abstract_module import AbstractModule
    #from application.api._direct_messages.welcome_messages import welcome_messages
    from twitter.application.subprocess.subroutines import filter
    from twitter.application.api._direct_messages.events import events
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_base_class import AbstractBase
    from application.api.superclass.abstract_module import AbstractModule
    #from application.api._direct_messages.welcome_messages import welcome_messages
    from application.subprocess.subroutines import filter
    from application.api._direct_messages.events import events
finally:
    from requests import get, post, delete

class mark_read(AbstractBase):
    '''Marks a message as read in the recipient’s Direct Message conversation 
view with the sender.

    - last_read_event_id
    The message ID of the most recent message to be marked read. All messages 
    before it will be marked read as well.
    
    - recipient_id
    The user ID of the user the message is from.'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, last_read_event_id=None, recipient_id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 last_read_event_id -> int; msg id
 recipient_id       -> int; user id'''

class indicate_typing(AbstractBase):
    '''Displays a visual typing indicator in the recipient’s Direct Message 
conversation view with the sender. Each request triggers a typing indicator 
animation with a duration of ~3 seconds.

A rudimentary approach would be to invoke an API request on every keypress or 
input event, however the application may quickly hit rate limits. A more 
sophisticated approach is to capture input events, but limit API requests to a 
specified interval based on the behavior of your users and the rate limit 
specified below.

    - recipient_id
    The user ID of the user to receive the typing indicator.'''

    def __init__(self):
        super().__init__()
        self._method = post

    def __call__(self, recipient_id=None):
        super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 recipient_id -> int; user id'''

# encapsulate namespace
direct_messages = AbstractModule(globals())
#setattr(direct_messages, 'welcome_messages', welcome_messages)
setattr(direct_messages, 'events', events)

# enforce singleton
del (mark_read, indicate_typing, events, #welcome_messages,
        
     AbstractBase, AbstractModule, get, post, delete)
