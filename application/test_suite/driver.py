from requests import ConnectionError, HTTPError
import time

def main(twitter, modules):

    #@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#
    """ ------------------------------------------- """
    """                   M A I N                   """
    """ ------------------------------------------- """
    #@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#
    
    ''' Local Declarations '''

    ### Slow down too many fast requests to server. ###
    SLEEP_TIME = 0 if twitter.mock else 5
    ERROR_TIME = 0 if twitter.mock else 300

    info_0 = '[TESTING]: {parent} module'
    info_1 = ('failed to test {parent} module'
              're-trying in {ERROR_TIME} seconds')
    info_2 = ' sleeping for {SLEEP_TIME} seconds'
    info_3 = 'completed package test with {failures} failure(s).'
    info_4 = ' All package modules succeeded!'
    info_5 = '[FAIL]: {parent} module'
    info_6 = '[PASS]: {parent} module'

    failures = 0 # count 

    # ----------------------------------------------------------------------- # 
    
    while modules:
        
        module = modules.pop()
        parent = module.__name__.split('.')[-1]
        twitter.log.info(info_0.format_map(vars(
            )))

        try:
            if module.test(twitter):
                failures += 1
                twitter.log.error(info_5.format_map(vars()))
            else:
                twitter.log.info(info_6.format_map(vars()))
        except (ConnectionError, HTTPError) as error:
            twitter.log.error(info_1.format_map(vars()))
            time.sleep(ERROR_TIME)
        else:
            if modules:
                twitter.log.info(info_2.format_map(vars()))
                time.sleep(SLEEP_TIME)

    # ----------------------------------------------------------------------- # 
    
    ''' Finished! '''

    # # # Display the System Wide Summary # # #
    if failures:
        twitter.log.error(info_3.format_map(vars()))
    else: twitter.log.info(info_4)

if __name__ == '__main__':
    pass
