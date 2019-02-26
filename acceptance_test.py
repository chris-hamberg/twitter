from application.subprocess.subroutines import locator, clear
from application import test_suite
from pprint import pprint
import sys, os

relpath = os.path.join('application', 'test_suite', 'test.log')
LOG_FILE = locator(relpath, True)
MODULES = {
         1: test_suite.modules.account,
         2: test_suite.modules.application,
         3: test_suite.modules.blocks,
         4: test_suite.modules.collections,
         5: test_suite.modules.direct_messages,
         6: test_suite.modules.favorites,
         7: test_suite.modules.followers,
         8: test_suite.modules.friends,
         9: test_suite.modules.friendships,
        10: test_suite.modules.geo,
        11: test_suite.modules.lists,
        12: test_suite.modules.media,        
        13: test_suite.modules.mutes,
        14: test_suite.modules.saved_searches,
        15: test_suite.modules.statuses,
        16: test_suite.modules.trends,
        17: test_suite.modules.users
        }

try:
    assert not os.path.exists(LOG_FILE)
except AssertionError:
    os.remove(LOG_FILE)
finally:
    from twitter import Twitter

class CLI:

    def __init__(self, space, message, first_choice, iterable, function):
        self.choice = None
        self.space  = space
        self.first_choice = first_choice
        self.iterable     = iterable
        self.function     = function
        self.message      = message

    def prompt(self, name=None):

        valid = lambda choice: choice in self.space

        while not valid(self.choice):
            
            clear()
            
            print('########################################')
            print('# --- {self.message} --- #'.format_map(vars()))
            print('########################################')
            print(self.first_choice.format_map(vars()))
    
            for e, key in self.iterable():
                e += 1
                line = self.function(key)
                print(' {e}. {line}'.format_map(vars()))
            e += 1
            print(' {e}. Quit'.format_map(vars())) 
            
            self.validate_choice()
        
        return self.choice

    def validate_choice(self):
        try:
            self.choice = int(input('>>> '))
        except ValueError:
            clear()
            print('error: you must select a number from the list.')
            input('press any key to try again...\n')

def main():

    # --------------------------------------------------------------- #
    '''            Prompt user for which module to test             '''
    # --------------------------------------------------------------- #
    space        = list(range(len(MODULES)+2))
    message      = 'Select which modules to test'
    first_choice = ' 0. THE ENTIRE LIBRARY'
    iterable = lambda: enumerate(MODULES.keys())
    function = lambda key: MODULES[key].__name__.split('.')[-1]
   
    cli = CLI(space=space, message=message, first_choice=first_choice, 
              iterable=iterable, function=function)

    entry = cli.prompt()

    if entry is len(MODULES)+1:
        sys.exit('Exiting automated test suite.')

    module_name = MODULES[entry].__name__ if entry is not 0 else 'ALL MODULES'
    modules = [MODULES[entry]] if entry is not 0 else list(MODULES.values())


    # --------------------------------------------------------------- #
    '''               Prompt user for which test type               '''
    # --------------------------------------------------------------- #
    space        = [1, 2, 3]
    message      = '    Select the test type    '
    first_choice = 'preparing to test {name}'
    iterable = lambda: enumerate(['mock response', 'real response'])
    function = lambda key: key

    cli = CLI(space=space, message=message, first_choice=first_choice,
              iterable=iterable, function=function)

    entry = cli.prompt(module_name)

    if entry is 3:
        sys.exit('Exiting automated test suite.')


    # --------------------------------------------------------------- #
    '''                 Begin Automated Test Suite                  '''
    # --------------------------------------------------------------- #
    twitter = Twitter()
    twitter.login(twitter.accounts[0])
    twitter.mock = True if entry is 1 else False
    test_suite.driver.main(twitter, modules)

    ### Thus, completes the proof.
    if sys.platform in 'linux':
        os.system('less {LOG_FILE}'.format_map(globals()))
    sys.exit(0) # Q.E.D.

if __name__ == '__main__': 
    main()
