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

def add():
    
    user, request = User(), Requests()
   
    while request.is_invalid:
        user.populate_credentials()
        print('Validating the credentials may take a few minutes...\n')
        request(user)
        clear()

        if request.is_invalid:
            try_again()
        else:
            user.lock()
            with database as session:
                session.add(user)
                show_message(user)

def remove():
    
    user = database_select()

    if user.count():
        view(user)

        id = select(user)
        with database as session:
            query = session.query(User).filter(User.id == id)
            user = query.first()
            confirm_delete(user)
            query.delete()
            
def show():
    user = database_select()
    view(user)

def database_select():
    with database as session:
        user = session.query(User)
    return user


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
