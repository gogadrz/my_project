import re    # регулярные выражения

text = 'AV - Analystic Vidhua AV'

result = re.match(r'AV', text)  # поиск в начале строки по шаблону
print('Поиск в начале строки по шаблону:', result)
print(result.group(0))
print(result.start())
print(result.end())

result = re.match(r'Analystic', text)
print(result)

print('*' * 40)

result = re.search(r'Analystic', text)   # поиск в строке по шаблону
print('Поиск в строке по шаблону:', result)
print(result.group(0))


result = re.findall(r'AV', text)         # все совпадения по шаблону
print('Все совпадения по шаблону:', result)

print('*' * 40)

text2 = 'AV is largest Analystic community of India. India!'

result = re.sub(r'India', 'the World', text2)    # замена всех найденных шаблонов
print('Замена всех найденных шаблонов:', result)

print('=' * 60)

pattern = re.compile(r'AV')
result = pattern.findall(text)
print(result)
result2 = pattern.findall(text2)
print(result2)


