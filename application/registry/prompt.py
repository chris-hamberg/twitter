# NOTE used for debugging
# if __name__ != '__main__':
try:
    from twitter.application.registry.model import Requests, User
    from twitter.application.registry.model import OrderedDict
    from twitter.application.subprocess.subroutines import clear, wait
    from twitter.application.registry.functions import *
except ModuleNotFoundError as main:
    from application.registry.model import Requests, User
    from application.registry.model import OrderedDict
    from application.subprocess.subroutines import clear, wait
    from application.registry.functions import *
    from dbhelper import database
finally:
    import sqlalchemy, sys, os
    twitter = None

# NOTE used for debugging
'''
else:
    clear = lambda: None
    wait  = lambda: None
    from model import Requests, User
    from collections import OrderedDict
    from sqlalchemy import create_engine
    from functions import *
    database = create_engine('sqlite://')
'''

def add():
    
    user, request = User(), Requests()
   
    while request.is_invalid:
        user.populate_credentials()
        print('Validating the credentials may take a few minutes...\n')
        request(user)
        clear()

        # NOTE used for debugging
        #request._is_invalid = False #request(user)
        #user.name = 'ChrisHamberg'

        if request.is_invalid:
            try_again()
        else:
            user.lock()
            twitter._accounts.append(user)
            with database as session:
                session.add(user)
                session.commit()
            show_message(user)


def remove():
    
    users = database_select()

    if users.count():
        view(users)

        id = select(users)
        with database as session:
            query = session.query(User).filter(User.id == id)
            user = query.first()
            confirm_delete(user)
            query.delete()
            session.commit()
        twitter._accounts.pop(id)
           

def show():
    users = database_select()
    view(users)

def database_select():
    with database as session:
        users = session.query(User)
    return users


def prompt():
    ''' Top level prompt '''
    clear()
    print('#'*80)
    print('#' + ' '*21 +'Application OAuth Registration Menu'+ ' '*22 + '#')
    print('#'*80)
    return input('''
0: exit
1: add accounts
2: remove accounts
3: view registry

[select by number]: ''')

def exit():
    assert False

def main():

    function = OrderedDict({
        0: exit,
        1: add,
        2: remove,
        3: show,
        })
 
    while True:
        try:
            choice = int(prompt())
            function[choice]()
            wait()
        except (KeyboardInterrupt, EOFError) as ok:
            pass
        except (ValueError, KeyError) as invalid:
            pass
        except AssertionError: 
            break
