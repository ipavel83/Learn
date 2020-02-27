import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s- %(message)s')
#logging.basicConfig(filename=__file__+'log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)
#logging.disable(logging.INFO)
#logging.disable(logging.WARNING)
#logging.disable(logging.ERROR)
#logging.disable(logging.CRITICAL)

debug = logging.debug

def customDebug(*args, **kwargs):
    print('custom Debug:',*args, **kwargs) #comment print call to disable custom debug messages
    pass

customDebug('self made ducktape analog of logging')

debug('allmost begining of program')

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

debug('end of program?')