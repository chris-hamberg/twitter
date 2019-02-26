### hopelessly ugly code that belongs to the 
### twitter/application/registry/prompt.py module. Hidden away deep in the 
### recesses of its own model; the very gaze of which is said to turn mortal
### men to stone statues. Much the same as gazing at Medusa.
try:
    from twitter.application.subprocess.subroutines import clear, wait
except ModuleNotFoundError as main:
    from application.subprocess.subroutines import clear, wait

def try_again():
    if input(error_msg).lower() == 'n': ### prompt the user.
        clear()
        print('Account registration process terminated.')
        raise KeyboardInterrupt

def show_message(user):
    clear()
    print(f'{user.name} added to database registry.')

def view(users):
    clear()
    print('#'*80)
    print('#'+' '*29+'Registered Accounts'+' '*30+'#')
    print('#'*80)
    print(f'{users.count()} accounts(s) registered\n')
    for user in users:
        print(f'{user.id}. {user.name}')

def select(user):
    while True:        
        try:
            id = int(
            input('\nselect (by number) which account to delete. '
            '(0 to exit): '))
            assert 0 <= id <= user.count()
        except (AssertionError, ValueError) as invalid:
            clear(); print('selection must be a number in the list.'
            ); wait(); view(user)
        else:
            if id is 0: raise KeyboardInterrupt
            else: return id

def confirm_delete(user):
    if input(f'\nyou are deleting {user.name} from the application.'
              ' Is this correct? [y/N] ').lower() != 'y': 
        raise KeyboardInterrupt
    else: 
        clear(); print(f'{user.name} has been removed from registration')

success_msg = '''{user.name} is confirmed as authorized by Twitter. Do you want 
to add this account to the application? ('yes' is required in 
order to use the api library for this Twitter account).

[Y/n] Add {username} to the application registry?
>>> '''

error_msg = '''It seems that there is something wrong with the oauth 
authorization credentials that you have entered. This 
could be caused by any number of reasons including a 
bad connection, a server error, or a typographical
mistake in an entry field(s).

[Y/n] Attempt to add a registration again?
>>> '''
