import json
import logging


def load_loggings(config_path, loggings, log_level):
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
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            save_path = config['save_path']
            return save_path
    except Exception as e:
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
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
        assets_path = config['assets_path']
        title = assets_path['title']
        if_close = assets_path['if_close']
        with open(title, 'r', encoding='utf-8') as t:
            title = json.load(t)
            with open(if_close, 'r', encoding='utf-8') as i:
                if_close = json.load(i)
                return title, if_close