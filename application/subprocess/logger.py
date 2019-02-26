try:
    from twitter.application.subprocess.subroutines import locator
except ModuleNotFoundError as main:
    from application.subprocess.subroutines import locator
finally:
    import datetime, logging, sys, os

def logger():
   
    forest_fire()

    log = logging.getLogger(__name__)
    template = ' %(asctime)s - %(levelname)s @ %(filename)s [%(lineno)d]: %(message)s'
    
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setFormatter(logging.Formatter(template))
    log.addHandler(stream_handler)
   
    relpath = os.path.join('application', 'test_suite', 'test.log')
    fpath = locator(relpath)
    file_handler = logging.FileHandler(fpath, mode='a')
    file_handler.setFormatter(logging.Formatter(template))
    log.addHandler(file_handler)
    
    log.setLevel(logging.INFO)

    return log

def forest_fire():
    
    incinerate = lambda leaf: os.remove(leaf)

    epoch  = datetime.datetime.utcnow()
    nodes  = branches()
    memory = tree(nodes, 0, 'timestamp')
    
    try:
        with open(memory) as expiration:
            expiration = int(expiration.read())
        assert epoch.toordinal() < expiration

    except (AssertionError, ValueError) as forgotten:
    
        generate(epoch, memory)
        leaf = tree(nodes, 1, 'test.log')
        if os.path.exists(leaf):
            incinerate(leaf)

def tree(branch, index, leaf):
    root = locator(branch[index])
    return os.path.join(root, leaf)

def branches():
    leaves  = ('extras', 'test_suite')
    branch  = lambda child: os.path.join(
            'application', child)
    return [branch(child) for child in leaves]

def generate(epoch, memory):
    delta = datetime.timedelta(days=1)
    expiration = (epoch + delta).toordinal()
    with open(memory, 'w') as memory:
        memory.write(str(expiration))
