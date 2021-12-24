def add_song(song_list, special_list, add_name):
    for i_name in song_list:
        if add_name == i_name[0]:
            special_list.append(add_name)
            return i_name[1]
    print('Нет такой песни в исходном списке')
    return 0


violator_songs = [['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43], ['Personal Jesus', 4.56],
                  ['Halo', 4.9], ['Waiting for the Night', 6.07], ['Enjoy the Silence', 4.20],
                  ['Policy of Truth', 4.76], ['Blue Dress', 4.29], ['Clean', 5.83]]
special_songs = []
total_time = 0

songs_cnt = int(input('Сколько песен выбрать? '))

for i_song in range(songs_cnt):
    print('Название', i_song + 1, 'песни: ', end = '')
    song_name = input()
    total_time += add_song(violator_songs, special_songs, song_name)

print('Общее время звучания песен:', round(total_time, 2), 'минут')
