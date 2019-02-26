import inspect, time, sys, os

clear = lambda: os.system('cls'
        ) if ('win' in sys.platform
        ) else os.system('clear')

wait = lambda: input('\npress enter to continue...\n')

def exponential_backoff(api, attempt=4, delay=0.1):
    while attempt:
        yield attempt
        attempt -= 1
        if attempt is 3:
            twitter.log.info('cache failed')
        twitter.log.error('retrying with EBO {delay} ms'.format_map(vars(
            )))
        time.sleep(delay)
        delay *= 2

def filter(**namespace):
    del namespace['self'], namespace['__class__']
    return namespace

def locator(relpath, root=False):
    destination, target = str(), 'twitter'
    frame = inspect.currentframe()
    abspath = inspect.getouterframes(frame, 2)[1][1].split(os.sep)
    if root:
        abspath = os.path.dirname(__file__).split(os.sep)
    for node in abspath:
        destination += node + os.sep
        if node == target:
            break
    return os.path.join(destination, relpath)
