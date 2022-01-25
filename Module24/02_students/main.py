from students import Student
import os


def full_name(file_name):
    return os.path.abspath(os.path.join(os.path.curdir, file_name))


def get_student_names(file_name):
    try:
        with open(full_name(file_name), 'r', encoding='utf-8') as in_file:
            student_names = in_file.read()
    except FileNotFoundError:
        print('Файл {} не найден.'.format('students.txt'))

    return student_names


def main(file_name):
    student_names = get_student_names(file_name).split('\n')
    students = [Student(index, student_names[index]) for index in range(10)]

    for i_student in sorted(students, key=lambda student: student.GPA):
        i_student.show_info(True)


main('students.txt')
