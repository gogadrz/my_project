special_chars = '@№$%^&*()'
filename = input('Название файла: ')

if filename[0] in special_chars:
    print('Ошибка: название начинается на один из специальных символов')
elif not filename.endswith('.txt') and not filename.endswith('.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')
