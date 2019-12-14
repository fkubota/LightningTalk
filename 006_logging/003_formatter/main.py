# formatterについて

import logging
import numpy as np

# set
logger = logging.getLogger('test01')
logger.setLevel(logging.DEBUG)

# formatter
form = '%(asctime)s %(name)s line%(lineno)d [%(levelname)s] %(message)s'
formatter = logging.Formatter(form)

# stream
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
sh.setFormatter(formatter)
logger.addHandler(sh)

# test
a = np.arange(0, 11)

logger.info('----- start -----')

logger.debug(f'a = {a}')
logger.debug(f'length a = {len(a)}')
logger.info(f'sum = {a.sum()}')

logger.info('----- end   -----')
