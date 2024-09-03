
import setproctitle
setproctitle.setproctitle('vpn_crawler')
import logging
from src.crawler import *
from src.db import *
from src.utils import *
from src.push import *
from src.log_config import info_logger, error_logger
from confs import db_name, info_table




def run():
    info_logger.info('vpn_crawler run.py start')
    new_data = {}
    message = ''
    date_time, date, time = get_formatted_time()

    try:
        vpn_usage = crawler()
        info_logger.info('crawler() success')


    except Exception as e:
        error_logger.error(f"An error occurred in crawler.py: {e}", exc_info=True)
        info_logger.error(f"An error occurred in crawler.py: Please check error log")
        message = 'crawler error in run.py'

        error_flag = 'YES'
        latest_flag = 'NO'
        new_data = {
            "vpn_usage": 'error',
            "create_date": date,
            "create_time": time,
            "error_flag": error_flag,
            "latest_flag": latest_flag,
            "notify_flag": 'YES',
            "update_time": date_time
        }
        write_info(db_name, info_table, new_data)

        return message, 'YES'
    
    # Compare and write table
    error_flag = 'NO'
    latest_flag = 'NO'
    notify = 'NO'
    latest_data = read_latest_info(db_name, info_table)
    if latest_data["vpn_usage"] != vpn_usage:
        message = message + ' ' + f'VPN 用量: {latest_data["vpn_usage"]}->{vpn_usage}'
        latest_flag = 'YES'
        notify = 'YES'

    
    new_data = {
        "vpn_usage": vpn_usage,
        "create_date": date,
        "create_time": time,
        "error_flag": error_flag,
        "latest_flag": latest_flag,
        "notify_flag": notify,
        "update_time": date_time
    }
    # 修改表中latest数据
    if latest_flag == 'YES':  # 当前爬到的是latest_flag是YES,则修改表中原latest_flag为NO
        latest_data['update_time'] = date_time
        update_info(db_name, info_table, latest_data)
    # 新写入latest数据
    write_info(db_name, info_table, new_data)

    return message, notify
    



if __name__=='__main__':

    try:
        message, notify = run()
        info_logger.info('run.py success')
    except Exception as e:
        error_logger.error(f"An error occurred in run.py: {e}", exc_info=True)
        info_logger.error(f"An error occurred in run.py: Please check error log")
        message = 'Compare or write table error in run.py'
        notify = 'YES'

    if notify == 'YES':
        info_logger.info(message)
        try:
            status = pushover(message)
            info_logger.info('Message sent')
        except Exception as e:
            error_logger.error(f"An error occurred in pushover: {e}", exc_info=True)
            info_logger.error(f"An error occurred in pushover: Please check error log")
