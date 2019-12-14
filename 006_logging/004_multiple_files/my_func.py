# 複数ファイルの場合

import logging
import numpy as np

logger = logging.getLogger('func')
logger.setLevel(logging.DEBUG)


def my_sum(lst):
    logger.debug(f'list = {lst}')
    sum_ = lst.sum()
    logger.info(f'sum = {sum_}')
    return sum_

