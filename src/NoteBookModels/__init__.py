# NoteBookModels/__init__.py

# 按功能分组导入
from .colluages import add_colluage, delete_colluage, colluage_list
from .helps import if_close, about, help__
from .loads import load_loggings, load_saves, load_assets
from .open_file import save, open_
from .settings import font_color, back_color, font_size, window_alpha

# 可以给模块起别名以便于访问
import NoteBookModels.colluages as colluages_module
import NoteBookModels.settings as settings_module

__version__ = "1.2.2"
__author__ = "FeSo4a"

# 控制 * 导入时包含的内容
__all__ = [
    'add_colluage', 'delete_colluage', 'colluage_list',
    'if_close', 'about', 'help__',
    'load_loggings', 'load_saves', 'load_assets',
    'save', 'open_',
    'font_color', 'back_color', 'font_size', 'window_alpha',
    'colluages_module', 'settings_module'
]
