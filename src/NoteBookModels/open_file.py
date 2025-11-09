import logging
import tkinter as tk
import tkinter.messagebox as messagebox


def save(root_window, text):
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


def open_(root_window, text):
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
    open_window.transient(root_window)
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
