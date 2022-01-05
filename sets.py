data = [
    {'id': 10, 'user': 'Bob'},
    {'id': 11, 'user': 'Misha'},
    {'id': 12, 'user': 'Anton'},
    {'id': 10, 'user': 'Bob'},
    {'id': 11, 'user': 'Misha'}
]

unique_data = []
for i_dict in data:
    data_exist = False
    for unique_dict in unique_data:
        if unique_dict['id'] == i_dict['id']:
            data_exist = True
            break
    if not data_exist:
        unique_data.append(i_dict)
print(unique_data, '\n')

unique_data_dict = {i_dict['id']: i_dict for i_dict in data}
print(unique_data_dict.values())
