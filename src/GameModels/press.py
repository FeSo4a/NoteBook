import logging


def press(press_number, number, save_path):
    """
    处理按钮点击事件，增加点击次数并保存到文件

    参数:
        无

    返回值:
        int: press_number
    """
    press_number = press_number + 1
    # 将当前点击次数保存到save文件
    with open(save_path, 'w', encoding='utf-8') as save:
        save.write(str(press_number))
    number.config(text=f'已按下 {press_number} 次')
    logging.debug(f'Save: {press_number}')
    return press_number


def clear(number, save_path):
    """
    清零点击次数并保存到文件

    参数:
        无

    返回值:
        int: press_number
    """
    press_number = 0
    # 将清零后的次数保存到save文件
    with open(save_path, 'w', encoding='utf-8') as save:
        save.write(str(press_number))
    number.config(text=f'已按下 {press_number} 次')
    logging.debug(f'Save: {press_number}')
    return press_number
