import json
import logging
import random
import tkinter as tk
import tkinter.messagebox as messagebox

def if_close(root_window, if_closes):
    """
    处理程序关闭确认功能

    该函数会读取配置文件中的关闭提示语，随机选择一个作为确认对话框的提示信息，
    如果用户确认则关闭主窗口。

    参数:
        无

    返回值:
        无
    """
    # noinspection PyBroadException
    try:
        if_close = random.choice(if_closes)
    except Exception as e:
        # 如果读取配置文件失败，使用默认提示语
        if_close = "真的要退出吗？"
        logging.error(f'Error: {e}, using default config.')

    # 显示确认对话框，用户确认后关闭主窗口
    if messagebox.askokcancel('退出确认', if_close):
        root_window.destroy()


def about(root_window, config_path):
    """
    创建并显示"关于"对话框窗口
    该函数会读取配置文件中的作者、版本和GitHub信息，并在弹出窗口中显示

    参数:
        无

    返回值:
        无
    """
    about = tk.Toplevel(root_window)
    about.title('关于')
    about.resizable(False, False)

    about.grab_set()
    about.focus_set()

    # 尝试从配置文件中读取程序信息并显示在关于窗口中
    # noinspection PyBroadException
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            author = config['author']
            version = config['version']
            github = config['github']
            about_text = tk.Label(about, font=('', 12),
                                  text=f'NoteBook信息：\n作者：{author}\n版本：{version}\nGithub：{github}')
            about_text.grid(row=0, column=0)
    except Exception as e:
        about_text = tk.Label(about, font=('', 12),
                              text=f'NoteBook信息：\n作者：{author}\n版本：{version}\nGithub：{github}')
        about_text.grid(row=0, column=0)
        logging.error(f'Error: {e}')


def help__(root_window, help_):
    """
    创建并显示帮助窗口函数

    该函数创建一个顶层窗口用于显示帮助信息，窗口包含帮助文本内容。
    函数不接受参数，无返回值。

    参数:
        无

    返回值:
        无
    """
    # 创建帮助窗口并设置基本属性
    help_window = tk.Toplevel(root_window)
    help_window.title('帮助')
    help_window.resizable(False, False)

    help_window.grab_set()
    help_window.focus_set()

    # 创建帮助文本标签并放置到窗口中
    help_text = tk.Label(help_window, text=help_)
    help_text.grid(row=0, column=0)