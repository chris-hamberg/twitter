from application.extras.exceptions import NotAuthorizedError
from application.subprocess.subroutines import clear
from application.extras.banner import banner
from application.registry import prompt
from application.extras import doc
import sys

def registration_process():
    doc.document(True); prompt.main(); yield
    twitter.log.warning(' no account registered in db')
    twitter.log.warning('manual authorization required')
    twitter.log.warning('twitter.help() for help')

def initialize():
    procedure = registration_process()
    for registration_attempt in range(2):
        try: assert bool(twitter.accounts)
        except AssertionError as empty_registry:
            next(procedure); clear()
            print(banner)

def login():

    try:
        username = input('>>> Enter username: ')
        twitter.login(username
            ) if bool(username
            ) else twitter.login(twitter.accounts[0]
            )
    except (IndexError, NotAuthorizedError) as manual_login:
        twitter.log.warning(twitter.username)
    except (KeyboardInterrupt, EOFError) as ok:
        clear(); sys.exit(0)

def interactive(twitter):
    try: import IPython; IPython.embed()
    except ModuleNotFoundError as ipython_not_installed:
        twitter.log.info(ipython_not_installed)
        import code
        code.interact(local=locals())

def execute():
    try: 
        initialize()
        twitter.log.info(twitter.accounts)
    except StopIteration as finished:
        finished
    finally:
        login(); interactive(twitter)



    #TODO twitter.help()
