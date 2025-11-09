import logging
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk


def font_color(root_window, text, tk_colors, save_path):
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
    font_color_window.transient(root_window)

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
            with open(save_path['font'], 'w', encoding='utf-8') as f:
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


def back_color(root_window, text, tk_colors, save_path):
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
    back_color_window.transient(root_window)

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
            with open(save_path['back'], 'w', encoding='utf-8') as f:
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


def font_size(root_window, text, save_path):
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
    font_size_window.transient(root_window)

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

            with open(save_path['size'], 'w', encoding='utf-8') as f:
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


def window_alpha(root_window, save_path):
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
    window_alpha_window.transient(root_window)

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

            with open(save_path['alpha'], 'w', encoding='utf-8') as f:
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
