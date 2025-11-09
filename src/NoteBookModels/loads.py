import json
import logging


def load_loggings(config_path, loggings, log_level):
    """
    加载日志配置并初始化logging模块

    该函数首先尝试从指定的配置文件中加载日志配置，如果加载失败则使用默认配置。
    配置包括日志级别、输出格式、日志文件路径和文件模式等参数。

    参数:
        config_path (str): 日志配置文件的路径
        loggings (dict): 默认日志配置字典，当配置文件加载失败时使用
        log_level (dict): 日志级别映射字典，将配置文件中的级别字符串映射为logging模块的级别常量

    返回值:
        无返回值
    """
    # noinspection PyBroadException
    try:
        # 尝试从指定配置文件加载日志配置并初始化logging模块
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            logging.basicConfig(
                level=log_level[config['loggings']['level']],
                format=config['loggings']['format'],
                filename=config['loggings']['file'],
                filemode=config['loggings']['mode']
            )

            # 记录日志配置信息
            logging.info(f'Logging level: {config["loggings"]["level"]}')
            logging.info(f'Logging file: {config["loggings"]["file"]}')
            logging.info(f'Logging format: {config["loggings"]["format"]}')
            logging.info(f'Logging mode: {config["loggings"]["mode"]}')
            logging.info(f'Config path: {config_path}')
            logging.info(f'Config: {config}')

            logging.info('Logging started.')
    except Exception as e:
        # 当配置文件加载失败时，使用默认配置初始化logging模块并记录错误信息
        logging.basicConfig(
            level=log_level[loggings['loggings']['level']],
            format=loggings['loggings']['format'],
            filename=loggings['loggings']['file'],
            filemode=loggings['loggings']['mode']
        )
        logging.error(f'Error: {e}, using default config.')


def load_saves(config_path):
    """
    加载保存路径配置文件

    参数:
        config_path (str): 配置文件的路径

    返回:
        dict 或 str: 如果配置文件加载成功，返回配置中的save_path值；
                     如果加载失败，返回默认的保存路径字典
    """
    try:
        # 尝试读取配置文件并解析JSON
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            save_path = config['save_path']
            return save_path
    except Exception as e:
        # 配置文件加载失败时，使用默认保存路径
        save_path = {
            'colluages': '../saves/colluages.json',
            'back': '../saves/back.json',
            'font': '../saves/font.txt',
            'alpha': '../saves/alpha.txt',
            'size': '../saves/size.txt'
        }
        logging.error(f'Error: {e}, using default save path.')
        return save_path


def load_assets(config_path):
    """
    加载资产配置文件

    该函数根据配置文件路径，读取资产配置信息，包括标题和关闭状态配置

    参数:
        config_path (str): 配置文件的路径

    返回值:
        tuple: 包含两个元素的元组
            - title (dict): 标题配置数据
            - if_close (dict): 关闭状态配置数据
    """
    # 读取主配置文件，获取资产路径配置
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
        assets_path = config['assets_path']
        title = assets_path['title']
        if_close = assets_path['if_close']

        # 读取标题配置文件
        with open(title, 'r', encoding='utf-8') as t:
            title = json.load(t)

            # 读取关闭状态配置文件
            with open(if_close, 'r', encoding='utf-8') as i:
                if_close = json.load(i)
                return title, if_close
