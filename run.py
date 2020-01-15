from app import app
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('test_logger')

if __name__ == '__main__':
    logger.info('info level')
    logger.debug('debug level')
    logger.warning('warning level')
    logger.error('error level')
    logger.critical('critical level')
    app.run()
