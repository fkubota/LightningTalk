# log level
# 1. DEBUG: 動作確認などデバッグの記録
# 2. INFO: 正常動作の記録
# 3. WARNING: ログの定義名
# 4. ERROR: エラーなど重大な問題
# 5. CRITICAL: 停止などの致命的な問題

import logging

# create instance
logger = logging.getLogger('test01')

# setLevel
logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.INFO)
# logger.setLevel(logging.ERROR)

# 標準出力
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
logger.addHandler(sh)

# test
logger.debug('this is debug')
logger.info('this is info')
logger.error('this is error')
logger.critical('this is critical')
