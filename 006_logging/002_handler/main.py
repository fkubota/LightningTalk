# stream handler と file handlerについて

import logging
import numpy as np

# set
logger = logging.getLogger('test01')
logger.setLevel(logging.DEBUG)

# stream
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
logger.addHandler(sh)

# file
fh = logging.FileHandler('test_log.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

# test
a = np.arange(0, 11)
# a = range(11)

logger.info('----- start -----')

logger.debug(f'a = {a}')
logger.debug(f'type a = {type(a)}')
logger.debug(f'length a = {len(a)}')
logger.info(f'sum = {a.sum()}')

logger.info('----- end   -----')
