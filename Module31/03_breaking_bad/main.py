import requests
import json
from typing import ClassVar


def main(json_filename: str) -> None:

    url_episodes: str = 'https://breakingbadapi.com/api/deaths'

    req_episodes: ClassVar = requests.get(url_episodes)
    data_episodes: list = json.loads(req_episodes.text)

    max_deaths = dict()
    max_deaths['number_of_deaths'] = 0

    for index in range(len(data_episodes)):
        if data_episodes[index]['number_of_deaths'] > max_deaths['number_of_deaths']:
            max_deaths['season'] = data_episodes[index]['season']
            max_deaths['episode'] = data_episodes[index]['episode']
            max_deaths['number_of_deaths'] = data_episodes[index]['number_of_deaths']

    info_str: str = 'Максимальное количество смертей:\nСезон: {season}, Эпизод: {episode}, Количество смертей: {deaths}'.format(
        season = max_deaths['season'], episode = max_deaths['episode'], deaths = max_deaths['number_of_deaths'])

    print(info_str)

    with open(json_filename, 'w') as file:
        json.dump(max_deaths, file, indent = 4)

    print('\nИнформация сохранена в файл \'{f_name}\''.format(f_name=json_filename))


if __name__ == '__main__':
    main('deaths.json')
