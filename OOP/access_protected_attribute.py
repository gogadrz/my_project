class Person:
    __count = 0

    def __init__(self, name, age):
        Person.__count += 1
        self.__name = None
        self.set_name(name)
        self.__age = None
        self.set_age(age)

    def set_name(self, name):
        for i_name in name:
            if not i_name.isalpha():
                raise Exception('Name must contain only letters')
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            raise Exception('age must in range 1..99')

    def get_age(self):
        return self.__age

    def get_count(self):
        return self.__count


p = Person('Pent', 2)
print(p.get_name(), p.get_age())

p.set_name('Petr')
p.set_age(99)

print(p.get_name(), p.get_age())
p._Person__age = 150

print(p.get_age())

print('неправильный способ', p._Person__age)
p2 = Person('igor', 15)
print('count =', p.get_count())
print('count igor', p2.get_count())