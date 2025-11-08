import json
import logging
import tkinter as tk
import tkinter.messagebox as messagebox


def add_colluage(root_window, save_path):
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
            with open(save_path['colluages'], 'r', encoding='utf-8') as f:
                save = json.load(f)
                save.append({
                    'name': colluage_name,
                    'sex': colluage_sex,
                    'ip': colluage_ip
                })
                # noinspection PyAssignmentToLoopOrWithParameter
                with open(save_path['colluages'], 'w', encoding='utf-8') as f:
                    json.dump(save, f, ensure_ascii=False, indent=4)
                    messagebox.showinfo('添加成功', '协作者添加成功！')

        except Exception as e:
            messagebox.showerror('添加失败', '添加失败！')
            logging.error(f'Error: {e}')

        add_colluage_window.destroy()

    # 添加按钮
    add_colluage_button = tk.Button(add_colluage_window, text='添加', command=add_colluage_button_click)
    add_colluage_button.grid(row=4, column=0)


def delete_colluage(root_window, save_path):
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
        with open(save_path['colluages'], 'r', encoding='utf-8') as f:
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
            with open(save_path['colluages'], 'w', encoding='utf-8') as f:
                json.dump(colluages, f, ensure_ascii=False, indent=4)

            messagebox.showinfo('删除成功', f'协作者 {deleted_name} 删除成功！')
            delete_colluage_window.destroy()

        except Exception as e:
            messagebox.showerror('删除失败', f'删除失败：{e}')
            logging.error(f'Error deleting colluage: {e}')

    # 创建删除按钮
    delete_button = tk.Button(delete_colluage_window, text='删除', command=delete_colluage_button_click)
    delete_button.grid(row=len(colluages) + 1, column=0, pady=10)


def colluage_list(root_window, save_path):
    """
    创建并显示协作者列表窗口

    参数:
        root_window: tkinter根窗口对象，用于创建顶层窗口的父窗口

    返回值:
        无

    功能:
        1. 创建协作者列表的模态对话框
        2. 从JSON文件中读取协作者信息并在列表框中显示
        3. 处理文件读取异常情况
    """
    # 创建协作者列表窗口并设置标题
    colluages = tk.Toplevel(root_window)
    colluages.title('协作者列表')

    # 设置为模态窗口并创建列表框控件
    colluages.grab_set()
    colluages_list = tk.Listbox(colluages)
    colluages_list.pack(fill='both', expand=True)

    # 读取协作者信息文件并在列表框中显示
    try:
        with open(save_path['colluages'], 'r', encoding='utf-8') as f:
            colluage = json.load(f)
            for i in colluage:
                colluages_list.insert(tk.END, f"{i['name']} ({i['sex']}) - {i['ip']}")

    # 处理文件读取异常，显示错误提示并记录日志
    except Exception as e:
        messagebox.showerror('错误', '无法读取协作者列表！')
        logging.error(f'Error reading colluages: {e}')

