import logging
from confs import error_log, success_log


logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
# 创建一个新的文件处理程序（handler）用于记录正常日志
normal_file_handler = logging.FileHandler(success_log)
normal_file_handler.setLevel(logging.DEBUG)  # 设置级别为 DEBUG
normal_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# 创建一个新的文件处理程序（handler）用于记录错误日志
error_file_handler = logging.FileHandler(error_log)
error_file_handler.setLevel(logging.ERROR)  # 设置级别为 ERROR
error_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# 获取默认的日志记录器并添加处理程序
info_logger = logging.getLogger('info_logger')
info_logger.addHandler(normal_file_handler)
info_logger.setLevel(logging.DEBUG)
error_logger = logging.getLogger('error_logger')
error_logger.addHandler(error_file_handler)

def setup_logger(success_log, error_log):
    '''
    1.运行setup之后，可以通过以下方式获取logger
    import logging
    info_logger = logging.getLogger('info_logger')  'info_logger'是全局的名称
    error_logger = logging.getLogger('error_logger')  'error_logger'是全局的名称
    2.然后记录
    info_logger.info('ssss')
    info_logger.debug('ssss')
    error_logger.error('ssss')
    '''
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    # 创建一个新的文件处理程序（handler）用于记录正常日志
    normal_file_handler = logging.FileHandler(success_log)
    normal_file_handler.setLevel(logging.DEBUG)  # 设置级别为 DEBUG
    normal_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # 创建一个新的文件处理程序（handler）用于记录错误日志
    error_file_handler = logging.FileHandler(error_log)
    error_file_handler.setLevel(logging.ERROR)  # 设置级别为 ERROR
    error_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # 获取默认的日志记录器并添加处理程序
    info_logger = logging.getLogger('info_logger')
    info_logger.addHandler(normal_file_handler)
    error_logger = logging.getLogger('error_logger')
    error_logger.addHandler(error_file_handler)
    

    