import arrow

def get_formatted_time():
    current_time = arrow.now('Asia/Shanghai')
    # 获取当前时间
    # current_time = arrow.now()

    # 格式化为 'YYYYMMDD-HH:MM:SS'
    full_format = current_time.format('YYYYMMDD-HH:mm:ss')

    # 格式化为 'YYYYMMDD'
    date_format = current_time.format('YYYYMMDD')

    # 格式化为 'HH:MM:SS'
    time_format = current_time.format('HH:mm:ss')

    return full_format, date_format, time_format

if __name__=='__main__':
    print(get_formatted_time())