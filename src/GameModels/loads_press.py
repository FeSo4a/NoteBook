import json
import logging


def load_save_path(config_path):
    """
    从配置文件中加载保存路径

    参数:
        config_path (str): 配置文件的路径

    返回:
        str: 从配置文件中读取的保存路径，如果读取失败则返回默认路径
    """
    try:
        # 读取主配置文件，获取保存路径配置
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            save_path = config['save_path']['save']
            return save_path
    except Exception as e:
        logging.error(f'Error: {e}, using default save path.')
        return '../saves/PressDatas/save.json'


def load_backup_path(config_path):
    """
    加载备份文件路径配置

    从指定的配置文件中读取备份路径设置，如果读取失败则返回默认备份路径

    参数:
        config_path (str): 配置文件的路径

    返回:
        str: 备份文件的路径，如果配置读取失败则返回默认路径 '../saves/PressDatas/backup.json'
    """
    try:
        # 读取主配置文件，获取备份路径配置
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            backup_path = config['save_path']['backup']
            return backup_path
    except Exception as e:
        logging.error(f'Error: {e}, using default backup path.')
        return '../saves/PressDatas/backup.json'


def load_loggings(logs, config_path):
    """
    加载日志配置并初始化日志系统

    参数:
        logs: 日志级别映射字典，用于将配置文件中的字符串级别转换为logging模块的常量
        config_path: 配置文件路径，指向包含日志配置的JSON文件

    返回值:
        无返回值
    """
    # 读取配置文件并初始化日志系统
    try:
        # 打开并加载JSON格式的配置文件
        with open(config_path, 'r', encoding='utf-8') as config:
            config = json.load(config)
            # 从配置中获取日志级别，如果未设置则默认为info级别
            log_level = logs.get(config.get('loggings', {}).get('level', 'info'), logging.INFO)
            # 从配置中获取日志文件路径，如果未设置则使用默认路径
            filename = config.get('loggings', {}).get('filename', '../logs/PressLog.log')
            # 配置基础日志设置，包括日志级别和输出文件
            logging.basicConfig(level=log_level,
                                filename=filename)
            # 记录初始化日志
            logging.info('Init...')

    # 处理其他可能的异常情况
    except Exception as e:
        logging.error(e)


def load_save(save_path):
    """
    读取保存的游戏数据

    参数:
        save_path (str): 保存数据文件的路径

    返回值:
        int: 从保存文件中读取的数字，如果读取失败则返回0
    """
    # 读取保存的游戏数据
    try:
        # 打开并读取保存的数据文件
        with open(save_path, 'r', encoding='utf-8') as save:
            # 将读取的内容转换为整数并赋值给press_number变量
            press_number = int(save.read())
            # 记录成功加载保存数据的日志
            logging.info(f'Load save: {press_number}')
            return press_number

    # 处理其他可能的异常情况
    except Exception as e:
        press_number = 0
        logging.error(e)
        return press_number
