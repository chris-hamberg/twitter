# NOTE used for debugging
#if __name__ != '__main__' and __name__ != 'model':
try:
    from twitter.application.subprocess.subroutines import clear
    from twitter.dbhelper import database
except ModuleNotFoundError as main:
    from application.subprocess.subroutines import clear
    from dbhelper import database
finally:
    from sqlalchemy import Column, Integer, Text
    from requests_oauthlib import OAuth1
    from collections import OrderedDict
    import requests

# NOTE used for debugging
'''
else:
    clear = lambda: None
    from sqlalchemy import Column, Integer, Text, create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from requests_oauthlib import OAuth1
    from collections import OrderedDict
    from types import SimpleNamespace
    import requests

    engine = create_engine('sqlite://')
    database = SimpleNamespace()
    database.Model = declarative_base()
'''

#########################################################
# NOTE all of these classes are used by the prompt module
###### the Database class is also used by the Twitter 
###### class to manage account registration, for oauth.

class Requests:
    ### This is used by the prompt.py module to validate that the oauth
    ### credentials entered by a user, are in fact, correct. Its concept is 
    ### simple. If a request (made with the oauth credentials, of which, are 
    ### under inquisition) returns a response code 200, then those credentials
    ### are correct. Otherwise, the credentials may or may not be correct and
    ### the user is notified of that contingency.
    def __init__(self):
        self._url = ('https://api.twitter.com/1.1'
                    '/account/verify_credentials.json')
        self._headers = {'user-agent': 'Chrome/24.0.1312.27'}
        self._response = None
        self._is_invalid = True

    @property
    def url(self):
        return self._url

    @property
    def headers(self):
        return self._headers
    
    @property
    def response(self):
        return self._response

    @property
    def is_invalid(self):
        return self._is_invalid

    def __call__(self, user):
        ''' A special requests wrapper '''
        try:
            response = requests.get(
                    self.url, headers=self.headers, auth=user.auth)
            response.raise_for_status()
        except Exception as invalid:
            pass
        else:
            self._is_invalid = False
            user.name = response.json()['screen_name']
            self._response = response

class User(database.Model):

    #####################################################################
    '''   SQLAlchemy Object-Relational Mapper for Application Users   '''
    # NOTE ##############################################################
    # ---- 

    __tablename__ = 'user'

    id           = Column('id', Integer, primary_key=True, autoincrement=True)
    name         = Column('name', Text)
    api_key      = Column('api_key', Text)
    api_secret   = Column('api_secret', Text)
    access_token = Column('access_token', Text)
    token_secret = Column('token_secret', Text)

    def __init__(self, **kwargs):
        self.id           = kwargs.get('user_id', None)
        self.name         = kwargs.get('user_name', None)
        self.api_key      = kwargs.get('user_api_key', None)
        self.api_secret   = kwargs.get('user_api_secret', None)
        self.access_token = kwargs.get('user_access_token', None)
        self.token_secret = kwargs.get('user_token_secret', None)
        self.clear        = clear

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

    @property
    def auth(self):
        return OAuth1(
                self.api_key, self.api_secret, 
                self.access_token, self.token_secret
                )

    def populate_credentials(self):

        # Prompt the user to enter 
        # api_key, api_secret, access_token, token_secret
        # return field entries for validation
        
        banner = 'Add Accounts'
        banner = '{0}\n{1}{2}{3}{4}{1}\n{0}'.format(
                '#'*80, '#',' '*33,banner,' '*33)
        
        help_msg = ('(hint: use ctrl shift v to paste clipboard '
                    'contents into the terminal.)')
        
        fields = OrderedDict({
            0: lambda: input('\nEnter API KEY: '),
            1: lambda: input('\nEnter API SECRET: '),
            2: lambda: input('\nEnter ACCESS TOKEN: '),
            3: lambda: input('\nEnter TOKEN SECRET: ')     
            })
        
        # NOTE used for debugging
        #from application.registry.oauth import AUTH as fields

        def process(key):
            self.clear()
            print(banner)
            print(help_msg)
            return fields[key]() 
        data = [process(key) for key in fields]
        self.columns = dict()

        for e, attribute in enumerate((
            'api_key', 'api_secret', 'access_token', 'token_secret'
            )):
            setattr(self, attribute, data[e])
            self.columns[attribute] = data[e]
        self.clear()

    def lock(self):
        ### populate_credentials is deleted from an instance because it is no
        ### longer needed once that instance has been validated. Hence the name,
        ### 'lock'. Performing this procedure saves some space in memory,
        ### and helps in preventing accidental corruption.
        self.populate_credentials = None
        ### clear is deleted because clear is anonymous. pickle refuses
        ### to pickle an object consisting of an anonymous function.
        self.clear = None

# NOTE used for debugging
#if __name__ != '__main__' and __name__ != 'model':
database.create_tables()
