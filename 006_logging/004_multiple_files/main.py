# 複数ファイルでlogging

import logging
import numpy as np
from my_func import my_sum

# set
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)
logger_func = logging.getLogger('func')  # <---- 別のファイルのloggerを取得
logger_func.setLevel(logging.DEBUG)

# stream
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
logger.addHandler(sh)
logger_func.addHandler(sh)

# file
fh = logging.FileHandler('test_log.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger_func.addHandler(fh)

# test
logger.info('----- start -----')

a = np.arange(0, 11)
# a = range(11)
sum_ = my_sum(a)

logger.info('----- end   -----')

