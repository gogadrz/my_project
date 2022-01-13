players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

#     Все члены команды из команды А, которые отдыхают.
#     Все члены команды из группы B, которые тренируются.
#     Все члены команды из команды C, которые путешествуют.

print(players_dict)
print()

# print(players_dict[1]['team'])
list1 = [players_dict[index]['name']
         for index in players_dict
         if players_dict[index]['team'] == 'A' and players_dict[index]['status'] == 'Rest'
        ]

list2 = [players_dict[index]['name']
         for index in players_dict
         if players_dict[index]['team'] == 'B' and players_dict[index]['status'] == 'Training'
         ]

list3 = [players_dict[index]['name']
         for index in players_dict
         if players_dict[index]['team'] == 'C' and players_dict[index]['status'] == 'Travel'
         ]

list4 = [players_dict[index]['name']
         for index in players_dict
         if players_dict[index].get('boom', {}) and players_dict[index]['status'] == 'Travel'
         ]

print(list1)
print(list2)
print(list3)
print(list4)