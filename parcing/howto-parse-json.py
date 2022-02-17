import requests
import json


my_req = requests.get('https://swapi.dev/api/planets/3/')

print(my_req.text)  # вывести просто текст

data = json.loads(my_req.text)  # десериализация json

print(data)

# dump(s) load(s) - если s нет, значит работаем с файлом

# запишем в json файл
with open('my_test.json', 'w') as file:
    json.dump(data, file, indent=4)  # сериализация json
                                     # indent - структурировать отступы для каждого вложенного блока данных

# прочитаем из json файла
with open('my_test.json', 'r') as file:
    data = json.load(file)

# load лучше использовать после десериализации json

print(data)
