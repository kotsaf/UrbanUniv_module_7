import os
import time

for root, dirs, files in os.walk(r'D:\Projects\H\module_7'):
    for file in files:
        filepath = os.path.join(r'D:\Projects\H\module_6', 'module_6.py')
        filetime = os.path.getmtime(os.path.join(root, file))
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(os.path.join(root, file))
        parent_dir = os.path.dirname(os.path.join(root, file))
    print(
        f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
        f'Родительская директория: {parent_dir}')

# Вывод в консоль:
# Обнаружен файл: ЧЕРНОВИК.py, Путь: D:\Projects\H\module_6\module_6.py, Размер: 3909 байт, 
# Время изменения: 12.10.2024 18:41, Родительская директория: D:\Projects\H\module_7
