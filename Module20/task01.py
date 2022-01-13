def get_interests_and_sum_surnames(students_dict):
    hobbies = list()
    surnames_len = 0
    for _, stud_info in students_dict.items():
        for one_hobby in stud_info['interests']:
            hobbies.append(one_hobby)
        for one_surname in stud_info['surname']:
            surnames_len += len(one_surname)
    return hobbies, surnames_len


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

for student_id, student_info in students.items():
    print('{id} - {age}'.format(
        id=student_id,
        age=student_info['age']
    ))

hobbies, sur_len = get_interests_and_sum_surnames(students)

print()
for i_hobby in hobbies:
    print('{hobby}'.format(
        hobby=i_hobby
    ))

print('{len}'.format(
    len=sur_len
    ))
