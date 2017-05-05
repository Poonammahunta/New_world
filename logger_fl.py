'''import logging
import time
from logging.handlers import RotatingFileHandler

def create_rotating_log(path):
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler('my_log.log',maxBytes=20,backupCount=5)
    logger.addHandler(handler)

    for i in range(5):
        logger.info('This is a test log line')


if __name__ == '__main__':
    log_file = "test1.log"
    create_rotating_log(log_file)'''

'''import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# create a file handler
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)

#create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(message)s)')
handler .setFormatter(formatter)

#add the handler to the logger
logger.addHandler(handler)
logger.info('Hello Baby')'''


import logging
logger = logging.getLogger("Rotating log")
logger.setLevel(logging.INFO)

try:
    open('C:\\Users\\pmahunta\\Desktop\\new\\pep.txt','rb')
except:
    logger.error("Failed to open a file",exc_info=True)
                              
