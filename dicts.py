family_member_orig = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}

family_member = dict()
family_member['name'] = "Jane"
family_member['surname'] = "Doe"
family_member['hobbyes'] = []
family_member['age'] = 35
family_member['children'] = [{}]
family_member['hobbyes'] = ['running', 'sky diving', 'singing']
family_member['children'] = [
    {
        'name': 'Alice',
        'age': 6
    },
    {
        'name': 'Bob',
        'age': 8
    }
]

print(family_member_orig)
print(family_member)
names_lst = []
child_name = 'Bob' \
             ''
for i_children in range(len(family_member['children'])):
    # if 'Bob' in family_member['children'][i_children]['name']:
    #     print('ага')
    # else:
    #     print('неа')
    names_lst.append(family_member['children'][i_children]['name'])

if child_name in names_lst:
    print('Ребенок', child_name, 'есть в списке')
    print('Его полное имя', child_name, family_member['surname'])
else:
    print('Ребенка по имени', child_name, 'в списке нет')
