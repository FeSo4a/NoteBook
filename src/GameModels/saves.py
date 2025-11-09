import logging


def backup(press_number, backup_path):
    """
    将当前点击次数备份到backup文件

    参数:
        无

    返回值:
        无
    """
    # 将当前点击次数写入backup文件
    with open(backup_path, 'w', encoding='utf-8') as backup:
        backup.write(str(press_number))
    logging.debug(f'Backup: {press_number}')


def load(press_number, number, backup_path, save_path):
    """
    从backup文件加载点击次数，并同步到save文件

    参数:
        无

    返回值:
        无
    """

    # 从backup文件读取点击次数
    with open(backup_path, 'r', encoding='utf-8') as backup:
        press_number = int(backup.read())
    # 同步到save文件
    with open(save_path, 'w', encoding='utf-8') as save:
        save.write(str(press_number))
    number.config(text=f'已按下 {press_number} 次')
    logging.debug(f'Load: {press_number}')
    return press_number
