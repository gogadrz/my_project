import re


source = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'

pattern = re.compile(r'wo')

result = pattern.match(source)
print('Поиск шаблона в начале строки:', result)

result = pattern.search(source)
print('Поиск первого найденного совпадения по шаблону:', result)

print('Содержимое найденной подстроки:', result.group())
print('Начальная позиция:', result.start())
print('Конечная позиция:', result.end())

result = pattern.findall(source)
print('Список всех упоминаний шаблона:', result)

result = pattern.sub('ЗАМЕНА', source)
print('Текст после замены:', result)
