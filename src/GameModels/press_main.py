import logging
import tkinter as tk

# 使用相对导入
from . import loads_press
from . import press
from . import saves


def run_game():
    # 日志级别映射字典
    config_path = '../configs/PressConfig.json'
    logs = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    save_path = loads_press.load_save_path(config_path)
    backup_path = loads_press.load_backup_path(config_path)
    loads_press.load_loggings(logs, config_path)
    press_number = loads_press.load_save(loads_press.load_save_path(config_path))

    root = tk.Tk()
    root.title('按！')
    root.geometry('400x400')

    title = tk.Label(root, text='按下下面这个按钮！')
    number = tk.Label(root, text=f'已按下 {press_number} 次')

    title.pack_forget()
    number.pack_forget()
    title.pack(side='top')
    number.pack(side='top')

    def clear_():
        nonlocal press_number
        press_number = press.clear(number, save_path)

    def press_():
        nonlocal press_number
        press_number = press.press(press_number, number, save_path)

    def backup_():
        saves.backup(press_number, backup_path)

    def load_():
        nonlocal press_number
        press_number = saves.load(press_number, number, backup_path, save_path)

    # 创建清空记录按钮并放置在窗口底部
    button_clear = tk.Button(root, text='清空记录', command=clear_)
    button_clear.pack(side='bottom')

    # 创建按钮容器框架并放置在窗口底部
    button_frame = tk.Frame(root)
    button_frame.pack(side='bottom')

    # 创建主要操作按钮并放置在窗口中
    button_press = tk.Button(root, text='按介个按钮', command=press_)
    button_press.pack()

    # 在按钮框架内创建备份记录按钮并水平排列在左侧
    button_backup = tk.Button(button_frame, text='备份记录', command=backup_)
    button_backup.pack(side='left')

    # 在按钮框架内创建加载记录按钮并水平排列在左侧
    button_load = tk.Button(button_frame, text='加载记录', command=load_)
    button_load.pack(side='left')

    # 启动GUI事件循环
    root.mainloop()
