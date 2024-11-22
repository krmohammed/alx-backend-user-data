import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='ex.log', encoding='utf-8', level=logging.DEBUG)
logger.debug('this message should go to the log file')
logger.info('so should this')
logger.warning('and this, too')
logger.error('and non-ascii stuff, too, like ....')