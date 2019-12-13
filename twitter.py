try: # NOTE import as a package
    from twitter.application.api.superclass import abstract_base_class as ABC
    from twitter.application.subprocess.subroutines import locator, clear
    from twitter.application.extras.exceptions import NotAuthorizedError
    from twitter.application.subprocess.cache import RateLimitCache
    from twitter.application.subprocess.logger import logger
    from twitter.dbhelper import database
    from twitter.application.registry.model import User
    from twitter.application.extras.banner import banner
    from twitter.application.extras.doc import document
    import twitter.application.subprocess.base64encode
    import twitter.application.subprocess.connection
    import twitter.application
    from twitter.application.registry import prompt
    from twitter.application import api
except ModuleNotFoundError as main: # run as interactive software
    from application.api.superclass import abstract_base_class as ABC
    from application.subprocess.subroutines import locator, clear
    from application.extras.exceptions import NotAuthorizedError
    from application.subprocess.cache import RateLimitCache
    from application.subprocess.logger import logger
    from dbhelper import database
    from application.registry.model import User
    from application.extras.banner import banner
    from application.extras.doc import document
    import application.subprocess.base64encode
    import application.subprocess.connection
    from application.registry import prompt
    from application import api
finally:
    import sqlalchemy
    import pathlib, sys, os

class Twitter:
    '''
    Front facing interface for the twitter API endpoints,
    and OAuth.
    '''
    def __init__(self):
        
        self._log = logger()
        self.log.set_level = lambda level: self._log.setLevel(level.upper(
            ))
        self._name = hex(id(self))
        self.database  = database
        self._accounts = []

        ######### Import authorized users from registry. ##########
        with self.database as session:
            query = session.query(User)
            self._accounts.extend([
            User(**account) for account in session.execute(query)
            ])
        self.log.info('loaded application.registry.model.Database')
        self.username = 'Not logging in.'
        ###########################################################


        ############# Delegate authority to processes #############
        try:
            twitter.application.subprocess.base64encode.twitter = self
            twitter.application.subprocess.connection.twitter = self
            twitter.application.subprocess.subroutines.twitter = self
        except NameError as running_as_main:
            application.subprocess.base64encode.twitter = self
            application.subprocess.connection.twitter = self
            application.subprocess.subroutines.twitter = self
        finally:
            ABC.AbstractBase.twitter = self
            self.log.info('injected {self}'.format_map(vars(
                )))
        ###########################################################

        try:
            twitter.application.registry.prompt.twitter = self
        except NameError as running_as_main:
            application.registry.prompt.twitter = self


        ####################### The API ########################
        self.account         = api.account
        self.application     = api.application
        self.blocks          = api.blocks
        self.collections     = api.collections
        self.direct_messages = api.direct_messages
        self.favorites       = api.favorites 
        self.followers       = api.followers
        self.friends         = api.friends
        self.friendships     = api.friendships
        self.geo             = api.geo
        self.lists           = api.lists
        self.media           = api.media
        self.mutes           = api.mutes
        self.saved_searches  = api.saved_searches
        self.statuses        = api.statuses
        self.trends          = api.trends
        self.users           = api.users
        self.log.info(
                '{self._name} has been defined'.format_map(vars(
                    )))
        ########################################################

        self._auth = None
        self._mock = False
        self._sentinel = False

    ###########################################
    '''      M E T H O D S      ''' ###########
    ###########################################

    def __repr__(self):
        try:
            search, namespace = dir, twitter.application.api
        except NameError as running_as_main:
            search, namespace = dir, application.api
        finally:
            method = lambda name: not name.startswith('_')
            good   = lambda name: name is not 'superclass'
            prefix = 'API: {0}'
            comma  = ', '
            return prefix.format(
                   comma.join(
                   [name for name in search(namespace
                       ) if good(name) and method(name)
                       ]))

    def login(self, username=None, token=None):

        ################## Sync the subprocesses ####################
        self._cache = RateLimitCache()
        self._cache.twitter = self
        #############################################################
        ' # # # # # # # # # # # # # # # # # # # # # # # # # # # # # '
        '# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #'
        ' # # # # # # # # # # # # # # # # # # # # # # # # # # # # # '
        # NOTE Automated Authorization
        if username in self.accounts:
            self.username = username or self.accounts[0]
            user = list(filter(lambda user: user.name == self.username, 
                    self._accounts)
                    )[0]
            self._auth    = user.auth
        # NOTE Partial Manual Authorization 
        elif token:
            self._auth    = token
            self.username = self.account.verify_credentials(
                ).json()['screen_name']
        # NOTE Full Manual Authorization
        else:
            raise NotAuthorizedError
        #############################################################
        self.log.info('loaded OAuth {self.username}'.format_map(vars(
                )))

    def manage_accounts(self):
        ''' Provides an interface to the registry.database '''
        prompt.main(); clear()
        print(banner)

    @property
    def auth(self):
        ''' read access OAuth credentials '''
        return self._auth

    @property
    def cache(self):
        ''' provide read access to cache '''
        return self._cache

    @property
    def log(self):
        ''' provide log access '''
        return self._log

    @property
    def accounts(self):
        ''' view the accounts registered in the registry.database '''
        return [account.name for account in self._accounts]

    @property
    def mock(self):
        ##################################
        ''' Mock Responses For Testing '''
        ##################################
        return self._mock

    @mock.setter
    def mock(self, boolean):
        self._mock = boolean
        self.log.info('MOCK: {self.mock}'.format_map(vars(
            )))

    @property
    def CACHE_LOCKED(self):
        ''' Used by the cache '''
        return self._sentinel

    @CACHE_LOCKED.setter
    def CACHE_LOCKED(self, boolean):
        self._sentinel = boolean
        self.log.info('CACHE LOCKED: {self.CACHE_LOCKED}'.format_map(vars(
            )))

    @property # NOTE Provided for the UI
    def RATE_LIMITING(self):
        return not self.CACHE_LOCKED

    @RATE_LIMITING.setter
    def RATE_LIMITING(self, boolean):
        self.CACHE_LOCKED = not boolean

    def help(self):
        document()
        clear(); print(banner)

def main():
    from application.interactive import session
    clear(); print(banner)
    twitter = Twitter()
    application.interactive.session.twitter = twitter
    application.interactive.session.execute()

def test():
    twitter = Twitter()
    twitter.statuses.home_timeline()
    sys.exit(0)

if __name__ == '__main__':
    try:
        sys.argv[1]
    except IndexError:
        main()
    else:
        test()
