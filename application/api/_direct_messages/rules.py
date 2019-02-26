from application.api.superclass.abstract_base_class import AbstractBase
from application.api.superclass.abstract_module import AbstractModule
from application.subprocess.subroutines import filter
from requests import delete, post, get

class destroy(AbstractBase):
    '''Deletes a Welcome Message Rule by the given id.
    
    - id
    The id of the Welcome Message Rule that should be deleted.'''

    def __init__(self):
        super().__init__()
        self._method = delete

    def __call__(self, id=None):
        return super().__call__(**filter(**vars(
            )))

    def __repr__(self):
        return '''PARAMETERS
 id -> int; rule id'''

# encapsulate namespace
rules = AbstractModule(globals())

# enforce singleton
del (destroy, 
     AbstractBase, AbstractModule, delete, post, get)
