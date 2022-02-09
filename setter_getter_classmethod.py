class Person:
    YEAR = 2022

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    def __str__(self):
        return 'Name is {name}, age is {age}'.format(name=self._name, age=self._age)

    @classmethod
    def hello_world(cls):
        print('hello world {year}'.format(year=cls.YEAR))


people = Person('Tom', 33)
people.age = 35
print(people)
print(people.age)
people.hello_world()
