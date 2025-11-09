import logging
import random
import tkinter as tk

import NoteBookModels
import GameModels

config_path = '../configs/NoteBookConfig.json'
version = '未知'
author = 'FeSo4a'
github = 'https://github.com/FeSo4a'
title = 'NoteBook'
if_close = '真的要退出吗？'

help_ = '''
基本编辑快捷键
Ctrl+C: 复制选中文本
Ctrl+V: 粘贴剪贴板内容
Ctrl+X: 剪切选中文本
Ctrl+Z: 撤销上一次操作
Ctrl+Y: 重做被撤销的操作
Ctrl+A: 全选文本
导航快捷键
Ctrl+Home: 移动到文档开头
Ctrl+End: 移动到文档结尾
Ctrl+Left/Right: 按单词移动光标
Ctrl+Up/Down: 垂直滚动视图
选择快捷键
Shift+Arrow keys: 扩展选择文本
Ctrl+Shift+Left/Right: 按单词扩展选择
Ctrl+Shift+Home/End: 选择到文档开头或结尾
其他功能
Tab: 插入制表符或缩进选中文本
Enter: 插入新行
Delete/Backspace: 删除字符
'''

log_level = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

loggings = {
    'loggings': {
        'level': 'info',
        'file': '../logs/log.log',
        'mode': 'w',
        'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    }
}

tk_colors = [
    'white',  # 白色
    'black',  # 黑色
    'red',  # 红色
    'green',  # 绿色
    'blue',  # 蓝色
    'yellow',  # 黄色
    'orange',  # 橙色
    'purple',  # 紫色
    'pink',  # 粉色
    'brown',  # 棕色
    'gray',  # 灰色
    'cyan',  # 青色
    'magenta',  # 品红色
    'lightgray',  # 浅灰色
    'darkgray',  # 深灰色
    'lightblue',  # 浅蓝色
    'darkblue',  # 深蓝色
    'lightgreen',  # 浅绿色
    'darkgreen',  # 深绿色
    'lightcoral',  # 浅珊瑚色
    'darkred'  # 深红色
]

NoteBookModels.loads.load_loggings(config_path, loggings, log_level)
save_path = NoteBookModels.loads.load_saves(config_path)
assets_path = NoteBookModels.loads.load_assets(config_path)
titles = assets_path[0]
if_closes = assets_path[1]


def root_window_init():
    """
    初始化根窗口函数

    该函数负责初始化应用程序的主窗口，包括设置窗口标题等功能。
    从配置文件中读取标题列表并随机选择一个作为窗口标题。
    如果配置文件读取失败，则使用默认配置。

    参数:
        无

    返回值:
        无
    """
    # noinspection PyGlobalUndefined
    global root_window
    root_window = tk.Tk()
    try:
        # 读取配置文件，设置窗口标题
        with open(save_path['alpha'], 'r', encoding='utf-8') as j:
            alpha = j.read()
            title = random.choice(titles)

            root_window.title(title)
            root_window.attributes('-alpha', alpha)

            logging.info('Windows initialized.')
            logging.info(f'Version: {version}')
            logging.info(f'Title: {title}')

            logging.info('Ready.')

    except Exception as e:
        # 配置文件读取失败时的错误处理
        logging.error(f'Error: {e}, using default config.')

        root_window.title(title)
        root_window.attributes('-alpha', 1.0)

        logging.info('Windows initialized.')
        logging.info(f'Version: {version}')
        logging.info(f'Title: {title}')

        logging.info('Ready.')

    # 修改这里：使用 lambda 表达式传递回调函数
    root_window.protocol('WM_DELETE_WINDOW', lambda: NoteBookModels.helps.if_close(root_window, if_closes))


def menus_init():
    main_menu = tk.Menu(root_window)

    new_file = tk.Menu(main_menu, tearoff=0)
    new_file.add_command(label='打开', command=lambda: NoteBookModels.open_file.open_(root_window, text))
    new_file.add_command(label='保存', command=lambda: NoteBookModels.open_file.save(root_window, text))

    colluage = tk.Menu(main_menu, tearoff=0)
    colluage.add_command(label='添加', command=lambda: NoteBookModels.colluages.add_colluage(root_window, save_path))
    colluage.add_command(label='删除', command=lambda: NoteBookModels.colluages.delete_colluage(root_window, save_path))
    colluage.add_command(label='查看', command=lambda: NoteBookModels.colluages.colluage_list(root_window, save_path))

    setting = tk.Menu(main_menu, tearoff=0)
    setting.add_command(label='字体颜色',
                        command=lambda: NoteBookModels.settings.font_color(root_window, text, tk_colors, save_path))
    setting.add_command(label='背景颜色',
                        command=lambda: NoteBookModels.settings.back_color(root_window, text, tk_colors, save_path))
    setting.add_command(label='字体大小',
                        command=lambda: NoteBookModels.settings.font_size(root_window, text, save_path))
    setting.add_command(label='窗口透明度',
                        command=lambda: NoteBookModels.settings.window_alpha(root_window, save_path))

    game = tk.Menu(main_menu, tearoff=0)
    # 在 menus_init() 函数中修改游戏菜单项
    game.add_command(label='按！', command=lambda: GameModels.run_game())

    help_menu = tk.Menu(main_menu, tearoff=0)
    help_menu.add_command(label='关于', command=lambda: NoteBookModels.helps.about(root_window, config_path))
    help_menu.add_command(label='帮助', command=lambda: NoteBookModels.helps.help__(root_window, help_))
    help_menu.add_command(label='退出', command=lambda: NoteBookModels.helps.if_close(root_window, if_closes))

    main_menu.add_cascade(label='文件', menu=new_file)
    main_menu.add_cascade(label='同事', menu=colluage)
    main_menu.add_cascade(label='设置', menu=setting)
    main_menu.add_cascade(label='放松一会', menu=game)
    main_menu.add_cascade(label='帮助', menu=help_menu)

    root_window.config(menu=main_menu)


def text_init():
    """
    初始化文本编辑区域

    该函数创建一个文本控件并将其添加到主窗口中，用于显示和编辑文本内容。
    文本控件使用默认字体大小为12，不自动换行，并填充整个可用空间。

    参数:
        无

    返回值:
        无
    """
    # noinspection PyGlobalUndefined
    global text
    # 创建文本控件并设置基本属性：字体大小12，不自动换行
    try:
        with open(save_path['font'], 'r', encoding='utf-8') as f:
            font_color = f.read()
        with open(save_path['back'], 'r', encoding='utf-8') as f:
            back_color = f.read()
        with open(save_path['size'], 'r', encoding='utf-8') as f:
            font_size = int(f.read())
            text = tk.Text(root_window, font=('', font_size), wrap='none', fg=font_color)
            text.config(bg=back_color)

    except Exception as e:
        font_color = 'black'
        back_color = 'white'
        font_size = 12
        text = tk.Text(root_window, font=('', font_size), wrap='none', fg=font_color)
        text.config(bg=back_color)
        logging.error(f'Error: {e}, using default config.')

    # 将文本控件添加到窗口布局中，填充水平和垂直方向的所有可用空间
    text.pack(fill='both', expand=True)


def main():
    root_window_init()
    menus_init()
    text_init()
    root_window.mainloop()


if __name__ == '__main__':
    main()
