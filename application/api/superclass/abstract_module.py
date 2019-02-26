import abc

BAD_NAMES = (
        'AbstractBase', 
        'Base64',
        'Collision',
        'Empty',
        'Media',
        'Numeric',
        'Ternary'
        )

class AbstractModule(list):

    #NOTE
    ' # -------------------------------------------------------- # '
    ### Creates a Namespace named after the resource family and  ###
    ### populates that Namespace with its proper members.        ###
    ###                                                          ###
    ### This provides the CLI UI with and easily navigable tree, ###
    ### as defined by the twitter.com API.                       ###
    ' # ----------------------------------------------------   - # '

    #NOTE
    ''' 
    Ultimately this class represents a module namespace occuring in 
    the application/api directory. Of which can be referrenced by 
    dot notation using the name prescribed by Twitter.com, rather 
    than using the default __repr__ and default access point 
    provided as usual, by Python, for a module of object.
    '''
    def __init__(self, namespace):
        ''' populating my namespace with names '''
        for name, cls in namespace.items():
            if type(cls) == abc.ABCMeta:
                if name not in BAD_NAMES:
                    instance = cls()
                    setattr(self, name, instance)
                    self.append(instance)
                
    def __repr__(self):
        # ---------------------------------------------- #
        # Display the endpoints for this resource family #
        # ---------------------------------------------- #
        return 'API: ' + ', '.join(self.__dict__.keys(
            ))
