import json
import logging
import random
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk

config_path = '../config.json'
version = '未知'
author = 'FeSo4a'
github = 'https://github.com/FeSo4a'
title = 'Note Book'
if_close_ = "真的要退出吗？"
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
        with open(config_path, 'r', encoding='utf-8') as f:
            with open('../saves/alpha.txt', 'r', encoding='utf-8') as j:
                alpha = j.read()
            config = json.load(f)
            titles = config['titles']
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

    root_window.protocol('WM_DELETE_WINDOW', if_close)


def menus_init():
    main_menu = tk.Menu(root_window)

    new_file = tk.Menu(main_menu, tearoff=0)
    new_file.add_command(label='打开', command=open_)
    new_file.add_command(label='保存', command=save)

    colluage = tk.Menu(main_menu, tearoff=0)
    colluage.add_command(label='添加', command=add_colluage)
    colluage.add_command(label='删除', command=delete_colluage)
    colluage.add_command(label='查看', command=colluage_list)

    settings = tk.Menu(main_menu, tearoff=0)
    settings.add_command(label='字体颜色', command=font_color)
    settings.add_command(label='背景颜色', command=back_color)
    settings.add_command(label='字体大小', command=font_size)
    settings.add_command(label='窗口透明度', command=window_alpha)

    help_menu = tk.Menu(main_menu, tearoff=0)
    help_menu.add_command(label='关于', command=about)
    help_menu.add_command(label='帮助', command=help__)
    help_menu.add_command(label='退出', command=if_close)

    main_menu.add_cascade(label='文件', menu=new_file)
    main_menu.add_cascade(label='同事', menu=colluage)
    main_menu.add_cascade(label='设置', menu=settings)
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
        with open('../saves/font.txt', 'r', encoding='utf-8') as f:
            font_color = f.read()
        with open('../saves/back.txt', 'r', encoding='utf-8') as f:
            back_color = f.read()
        with open('../saves/size.txt', 'r', encoding='utf-8') as f:
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


def if_close():
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
        # 读取配置文件，获取关闭提示语列表并随机选择一个
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            if_close_ = config['if_close']
            if_close_ = random.choice(if_close_)
    except Exception as e:
        # 如果读取配置文件失败，使用默认提示语
        if_close_ = "真的要退出吗？"
        logging.error(f'Error: {e}, using default config.')

    # 显示确认对话框，用户确认后关闭主窗口
    if messagebox.askokcancel('退出确认', if_close_):
        root_window.destroy()


def save():
    """
    创建保存文件的对话框窗口

    该函数创建一个用于保存文件的图形界面窗口，包含文件路径和编码格式的输入框，
    以及相应的保存按钮。用户输入相关信息后可以将文本内容保存到指定文件。

    参数:
        无

    返回值:
        无
    """
    save = tk.Toplevel(root_window)
    save.title('保存')
    save.resizable(False, False)

    save.grab_set()  # 获取焦点并阻止其他窗口交互
    save.transient(root_window)  # 设置为父窗口的临时窗口
    save.focus_set()  # 设置焦点

    # 创建标签控件
    save_file_name = tk.Label(save, text='输入保存的文件地址：')
    save_encoding = tk.Label(save, text='输入保存的文件编码：')
    save_file_name.grid(row=0, column=0)
    save_encoding.grid(row=1, column=0)

    # 创建输入框控件
    save_file_name_entry = tk.Entry(save)
    save_encoding_entry = tk.Entry(save)
    save_file_name_entry.grid(row=0, column=1)
    save_encoding_entry.grid(row=1, column=1)

    def save_file():
        """
        执行文件保存操作的内部函数

        该函数获取文本内容和用户输入的文件路径、编码格式，
        将文本内容写入指定文件中，并显示保存结果提示信息。

        参数:
            无

        返回值:
            无
        """
        texts = text.get('1.0', 'end')
        try:
            file_name = save_file_name_entry.get()
            encoding = save_encoding_entry.get()
            with open(file_name, 'w', encoding=encoding) as f:
                f.write(texts)
            messagebox.showinfo('保存', '保存成功！')

        except Exception as e:
            messagebox.showerror('保存失败', f'保存失败：{e}')
            logging.error(f'Error: {e}')
        save.destroy()

    # 创建保存按钮
    save_button = tk.Button(save, text='保存', command=save_file)
    save_button.grid(row=2, column=0)

    save.mainloop()


def open_():
    """
    打开文件对话框函数
    创建一个顶层窗口用于输入文件路径和编码格式，然后读取并显示文件内容

    参数:
        无

    返回值:
        无
    """
    # 创建打开文件的顶层窗口并设置基本属性
    open_window = tk.Toplevel(root_window)
    open_window.title('打开')
    open_window.resizable(False, False)

    # 设置窗口焦点并捕获所有事件
    open_window.grab_set()
    open_window.focus_set()

    # 创建文件路径和编码格式的标签
    open_file_name = tk.Label(open_window, text='输入加载的文件地址：')
    open_encoding = tk.Label(open_window, text='输入加载的文件编码：')
    open_file_name.grid(row=0, column=0)
    open_encoding.grid(row=1, column=0)

    # 创建文件路径和编码格式的输入框
    open_file_name_entry = tk.Entry(open_window)
    open_encoding_entry = tk.Entry(open_window)
    open_file_name_entry.grid(row=0, column=1)
    open_encoding_entry.grid(row=1, column=1)

    def open_file():
        """
        执行文件打开操作的内部函数
        获取用户输入的文件路径和编码格式，读取文件内容并显示在文本框中

        参数:
            无

        返回值:
            无
        """
        try:
            # 获取用户输入的文件名和编码格式
            file_name = open_file_name_entry.get()
            encoding = open_encoding_entry.get()
            # 以只读模式打开文件并读取内容
            with open(file_name, 'r', encoding=encoding) as f:
                text.delete('1.0', 'end')
                text.insert('1.0', f.read())
                messagebox.showinfo('打开', '文件打开成功！')
        except Exception as e:
            # 处理文件打开异常情况
            messagebox.showerror('打开失败', f'打开失败：{e}')
            logging.error(f'Error: {e}')
        # 关闭打开文件窗口
        open_window.destroy()

    # 创建打开按钮并绑定点击事件
    open_button = tk.Button(open_window, text='打开', command=open_file)
    open_button.grid(row=2, column=0)
    open_window.mainloop()


def about():
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


def add_colluage():
    """
    创建并显示“添加协作者”窗口，允许用户输入协作者的姓名、性别和IP地址，
    并将这些信息保存到JSON配置文件中。

    参数:
        无

    返回值:
        无
    """

    # 创建顶层窗口
    add_colluage_window = tk.Toplevel(root_window)
    add_colluage_window.title('添加协作者')
    add_colluage_window.resizable(False, False)
    add_colluage_window.grab_set()
    add_colluage_window.focus_set()

    # 姓名输入框及相关标签
    name_label = tk.Label(add_colluage_window, text='请输入协作者名称：')
    name_label.grid(row=0, column=0)
    name = tk.StringVar()
    name.set('')
    name_entry = tk.Entry(add_colluage_window, textvariable=name)
    name_entry.grid(row=0, column=1)

    # 性别选择单选按钮及相关标签
    sex = tk.StringVar()
    sex.set('男')
    sex_label = tk.Label(add_colluage_window, text='请选择协作者性别：')
    sex_label.grid(row=2, column=0)
    sex_radio_button = tk.Radiobutton(add_colluage_window, text='男', variable=sex, value='男')
    sex_radio_button.grid(row=2, column=1)
    sex_radio_button = tk.Radiobutton(add_colluage_window, text='女', variable=sex, value='女')
    sex_radio_button.grid(row=2, column=2)

    # IP地址输入框及相关标签
    ip = tk.StringVar()
    ip_label = tk.Label(add_colluage_window, text='请输入协作者IP：')
    ip_label.grid(row=3, column=0)
    ip_entry = tk.Entry(add_colluage_window, textvariable=ip)
    ip_entry.grid(row=3, column=1)

    def add_colluage_button_click():
        """
        添加协作者按钮点击事件处理函数
        该函数会获取用户输入的协作者信息，并添加到配置文件中

        参数:
            无

        返回值:
            无
        """
        colluage_name = name.get()
        colluage_sex = sex.get()
        colluage_ip = ip.get()
        if colluage_name == '' or colluage_sex == '' or colluage_ip == '':
            messagebox.showerror('添加失败', '请填写完整的信息！')
            add_colluage_window.destroy()
            return

        try:
            with open('../saves/colluages.json', 'r', encoding='utf-8') as f:
                save = json.load(f)
                save.append({
                    'name': colluage_name,
                    'sex': colluage_sex,
                    'ip': colluage_ip
                })
                # noinspection PyAssignmentToLoopOrWithParameter
                with open('../saves/colluages.json', 'w', encoding='utf-8') as f:
                    json.dump(save, f, ensure_ascii=False, indent=4)
                    messagebox.showinfo('添加成功', '协作者添加成功！')

        except Exception as e:
            messagebox.showerror('添加失败', '添加失败！')
            logging.error(f'Error: {e}')

        add_colluage_window.destroy()

    # 添加按钮
    add_colluage_button = tk.Button(add_colluage_window, text='添加', command=add_colluage_button_click)
    add_colluage_button.grid(row=4, column=0)


def delete_colluage():
    """
    删除协作者功能函数
    创建一个窗口用于选择并删除协作者

    功能说明：
    - 打开一个新的模态窗口供用户选择要删除的协作者
    - 从本地JSON文件中加载协作者列表
    - 用户通过单选按钮选择要删除的协作者
    - 删除后将更新后的列表重新保存到文件中

    异常处理：
    - 若无法读取协作者文件，则弹出错误提示并记录日志
    - 若删除过程中发生异常，也会进行相应提示与日志记录

    注意事项：
    - 窗口为模态窗口，会阻塞主窗口操作
    - 若没有协作者可删除，将直接关闭窗口并给出提示
    """

    # 创建删除协作者的顶层窗口，并设置基本属性
    delete_colluage_window = tk.Toplevel(root_window)
    delete_colluage_window.title('删除协作者')
    delete_colluage_window.resizable(False, False)
    delete_colluage_window.grab_set()
    delete_colluage_window.focus_set()

    # 读取协作者列表
    try:
        with open('../saves/colluages.json', 'r', encoding='utf-8') as f:
            colluages = json.load(f)
    except Exception as e:
        messagebox.showerror('错误', '无法读取协作者列表！')
        logging.error(f'Error reading colluages: {e}')
        delete_colluage_window.destroy()
        return

    # 检查是否有协作者可供删除
    if not colluages:
        messagebox.showinfo('提示', '暂无协作者可删除！')
        delete_colluage_window.destroy()
        return

    # 创建协作者选择变量
    selected_colluage = tk.StringVar()

    # 创建标签
    select_label = tk.Label(delete_colluage_window, text='请选择要删除的协作者：')
    select_label.grid(row=0, column=0, columnspan=2)

    # 创建单选框列表，显示所有协作者信息（姓名、性别、IP）
    for i, colluage in enumerate(colluages):
        colluage_text = f"{colluage['name']} ({colluage['sex']}) - {colluage['ip']}"
        radio = tk.Radiobutton(delete_colluage_window,
                               text=colluage_text,
                               variable=selected_colluage,
                               value=i)
        radio.grid(row=i + 1, column=0, columnspan=2, sticky='w')

    # 设置默认选中第一个协作者
    if colluages:
        # noinspection PyTypeChecker
        selected_colluage.set(0)

    def delete_colluage_button_click():
        """
        删除协作者按钮点击事件处理函数

        功能说明：
        - 获取当前选中的协作者索引
        - 从内存列表中移除该协作者
        - 将更新后的列表写回JSON文件
        - 提示删除成功或失败的信息

        异常处理：
        - 处理类型转换异常及文件写入异常
        """

        try:
            index = int(selected_colluage.get())
            deleted_name = colluages[index]['name']

            # 从列表中删除选中的协作者
            colluages.pop(index)

            # 保存更新后的列表
            with open('../saves/colluages.json', 'w', encoding='utf-8') as f:
                json.dump(colluages, f, ensure_ascii=False, indent=4)

            messagebox.showinfo('删除成功', f'协作者 {deleted_name} 删除成功！')
            delete_colluage_window.destroy()

        except Exception as e:
            messagebox.showerror('删除失败', f'删除失败：{e}')
            logging.error(f'Error deleting colluage: {e}')

    # 创建删除按钮
    delete_button = tk.Button(delete_colluage_window, text='删除', command=delete_colluage_button_click)
    delete_button.grid(row=len(colluages) + 1, column=0, pady=10)


def colluage_list():
    colluages = tk.Toplevel(root_window)
    colluages.title('协作者列表')

    colluages.grab_set()
    colluages_list = tk.Listbox(colluages)
    colluages_list.pack(fill='both', expand=True)

    try:
        with open('../saves/colluages.json', 'r', encoding='utf-8') as f:
            colluage = json.load(f)
            for i in colluage:
                colluages_list.insert(tk.END, f"{i['name']} ({i['sex']}) - {i['ip']}")

    except Exception as e:
        messagebox.showerror('错误', '无法读取协作者列表！')
        logging.error(f'Error reading colluages: {e}')


def help__():
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


def font_color():
    """
    创建字体颜色设置窗口函数

    该函数创建一个顶层窗口，允许用户选择字体颜色并保存设置。
    用户可以从下拉框中选择预定义的颜色，然后应用并保存到配置文件中。

    参数:
        无

    返回值:
        无
    """
    # 创建字体颜色设置的顶层窗口
    font_color_window = tk.Toplevel(root_window)
    font_color_window.title('字体颜色')
    font_color_window.resizable(False, False)

    # 设置窗口焦点和模态特性
    font_color_window.grab_set()
    font_color_window.focus_set()

    # 创建标签和颜色选择下拉框
    font_color_label = tk.Label(font_color_window, text='请选择字体颜色：')
    font_color_label.grid(row=0, column=0)

    color = tk.StringVar()
    font_color_box = ttk.Combobox(font_color_window, values=tk_colors, textvariable=color)
    font_color_box.grid(row=0, column=1)

    def change_font_color():
        """
        应用并保存字体颜色设置的内部函数

        获取用户选择的颜色，应用到文本组件，并将设置保存到文件中。
        如果保存过程中出现异常，则显示错误信息。
        """
        try:
            font_color = color.get()
            text.config(fg=font_color)
            with open('../saves/font.txt', 'w', encoding='utf-8') as f:
                f.write(f'{font_color}')
                messagebox.showinfo('成功', '设置已保存！')
                font_color_window.destroy()

        except Exception as e:
            messagebox.showerror('错误', '无法保存设置！')
            logging.error(f'Error saving settings: {e}')
            font_color_window.destroy()

    # 创建应用设置按钮
    change_font_color_button = tk.Button(font_color_window, text='应用并保存设置', command=change_font_color)
    change_font_color_button.grid(row=1, column=0)


def back_color():
    """
    创建背景颜色设置窗口函数

    该函数创建一个顶层窗口，允许用户选择背景颜色并保存设置。
    用户可以从下拉框中选择预定义的颜色，然后应用并保存到配置文件中。

    参数:
        无

    返回值:
        无
    """
    # 创建背景颜色设置的顶层窗口
    back_color_window = tk.Toplevel(root_window)
    back_color_window.title('字体颜色')
    back_color_window.resizable(False, False)

    # 设置窗口焦点和模态特性
    back_color_window.grab_set()
    back_color_window.focus_set()

    # 创建标签和颜色选择下拉框
    back_color_label = tk.Label(back_color_window, text='请选择字体颜色：')
    back_color_label.grid(row=0, column=0)

    color = tk.StringVar()
    back_color_box = ttk.Combobox(back_color_window, values=tk_colors, textvariable=color)
    back_color_box.grid(row=0, column=1)

    def change_back_color():
        """
        应用并保存背景颜色设置的内部函数

        获取用户选择的颜色，应用到文本组件，并将设置保存到文件中。
        如果保存过程中出现异常，则显示错误信息。
        """
        try:
            back_color = color.get()
            text.config(bg=back_color)
            with open('../saves/back.txt', 'w', encoding='utf-8') as f:
                f.write(f'{back_color}')
                messagebox.showinfo('成功', '设置已保存！')
                back_color_window.destroy()

        except Exception as e:
            messagebox.showerror('错误', '无法保存设置！')
            logging.error(f'Error saving settings: {e}')
            back_color_window.destroy()

    # 创建应用设置按钮
    change_back_color_button = tk.Button(back_color_window, text='应用并保存设置', command=change_back_color)
    change_back_color_button.grid(row=1, column=0)


def font_size():
    """
    创建字体大小设置窗口函数

    该函数创建一个顶层窗口，允许用户选择字体大小并保存设置。
    用户可以从下拉框中选择预定义的字体大小，然后应用并保存到配置文件中。

    参数:
        无

    返回值:
        无
    """
    # 创建字体大小设置的顶层窗口
    font_size_window = tk.Toplevel(root_window)
    font_size_window.title('字体大小')
    font_size_window.resizable(False, False)

    # 设置窗口焦点和模态特性
    font_size_window.grab_set()
    font_size_window.focus_set()

    # 创建标签和字体大小选择下拉框
    font_size_label = tk.Label(font_size_window, text='请选择字体大小：')
    font_size_label.grid(row=0, column=0)

    # 定义常用的字体大小选项
    font_sizes = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
    size = tk.StringVar()
    font_size_box = ttk.Combobox(font_size_window, values=font_sizes, textvariable=size)
    font_size_box.grid(row=0, column=1)

    def change_font_size():
        """
        应用并保存字体大小设置的内部函数

        获取用户选择的字体大小，应用到文本组件，并将设置保存到文件中。
        如果保存过程中出现异常，则显示错误信息。
        """
        try:
            font_size = int(size.get())
            # 获取当前字体名称，只改变字体大小
            current_font = text.cget('font')
            if isinstance(current_font, str):
                # 如果是字符串格式的字体定义
                text.config(font=(current_font, font_size))
            else:
                # 如果是元组格式的字体定义
                text.config(font=(current_font[0], font_size))

            with open('../saves/size.txt', 'w', encoding='utf-8') as f:
                f.write(f'{font_size}')
                messagebox.showinfo('成功', '设置已保存！')
                font_size_window.destroy()

        except Exception as e:
            messagebox.showerror('错误', '无法保存设置！')
            logging.error(f'Error saving settings: {e}')
            font_size_window.destroy()

    # 创建应用设置按钮
    change_font_size_button = tk.Button(font_size_window, text='应用并保存设置', command=change_font_size)
    change_font_size_button.grid(row=1, column=0)


def window_alpha():
    """
    创建窗口透明度设置窗口函数

    该函数创建一个顶层窗口，允许用户调整主窗口的透明度并保存设置。
    用户可以从下拉框中选择预定义的透明度值，然后应用并保存到配置文件中。

    参数:
        无

    返回值:
        无
    """
    # 创建窗口透明度设置的顶层窗口
    window_alpha_window = tk.Toplevel(root_window)
    window_alpha_window.title('窗口透明度')
    window_alpha_window.resizable(False, False)

    # 设置窗口焦点和模态特性
    window_alpha_window.grab_set()
    window_alpha_window.focus_set()

    # 创建标签和透明度选择下拉框
    window_alpha_label = tk.Label(window_alpha_window, text='请选择窗口透明度：')
    window_alpha_label.grid(row=0, column=0)

    # 定义常用的透明度选项 (0.0-1.0, 1.0为完全不透明)
    alpha_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    alpha = tk.StringVar()
    # noinspection PyTypeChecker
    window_alpha_box = ttk.Combobox(window_alpha_window, values=alpha_values, textvariable=alpha)
    window_alpha_box.grid(row=0, column=1)

    def change_window_alpha():
        """
        应用并保存窗口透明度设置的内部函数

        获取用户选择的透明度值，应用到主窗口，并将设置保存到文件中。
        如果保存过程中出现异常，则显示错误信息。
        """
        try:
            alpha_value = float(alpha.get())
            root_window.attributes('-alpha', alpha_value)

            with open('../saves/alpha.txt', 'w', encoding='utf-8') as f:
                f.write(f'{alpha_value}')
                messagebox.showinfo('成功', '设置已保存！')
                window_alpha_window.destroy()

        except Exception as e:
            messagebox.showerror('错误', '无法保存设置！')
            logging.error(f'Error saving settings: {e}')
            window_alpha_window.destroy()

    # 创建应用设置按钮
    change_window_alpha_button = tk.Button(window_alpha_window, text='应用并保存设置', command=change_window_alpha)
    change_window_alpha_button.grid(row=1, column=0)


def main():
    root_window_init()
    menus_init()
    text_init()
    root_window.mainloop()


if __name__ == '__main__':
    main()
