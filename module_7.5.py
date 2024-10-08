import os
import time

for root, dirs, files in os.walk('.'):
  for file in files:
    filepath = os.walk('.')
    filetime = os.path.getmtime('.')
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize('.')
    parent_dir = os.path.dirname('.')
  print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')