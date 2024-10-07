def custom_write(file_name, strings):
    name = file_name
    strings_positions = {}
    str_num = 0

    for i in strings:
        file = open(name, 'r', encoding='utf_8')
        file.read()
        str_bite = file.tell()
        str_num += 1
        strings_positions[(str_num, str_bite)] = f'{i}'
        file.close()

        file = open(name, 'a', encoding = 'utf_8')  # r, w, a - режимы чтения (read, write, append)
        file.write(f'{i}\n')

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('text.txt', info)
for elem in result.items():
  print(elem)


'''Вывод на консоль'''
# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')

'''Файл после запуска'''
# Text for tell.
# Используйте кодировку utf-8.
# Because there are 2 languages!
# Спасибо!
