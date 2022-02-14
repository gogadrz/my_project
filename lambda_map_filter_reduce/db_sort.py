import copy


class Db:
    __name = None
    __sur = None
    __age = None
    __users = list()
    user = dict()

    def add_user(self, name, sur, age):
        self.user['name'] = name
        self.user['sur'] = sur
        self.user['age'] = age
        self.__users.append(copy.deepcopy(self.user))
        pass

    @property
    def name(self):
        return self.__name

    @property
    def sur(self):
        return self.__sur

    @property
    def age(self):
        return self.__age

    def print_users(self):
        for i in self.__users:
            print(i)

    def print_sorted(self):
        for i_user in sorted(self.__users, key=lambda age: int(age['age'])):
            print(i_user)


my_users = Db()
my_users.add_user(name = 'Karl', sur = 'Parfenov', age = '59')
my_users.add_user(name = 'Ivan', sur = 'Volopaef', age = '14')
my_users.add_user(name = 'Serg', sur = 'Balabued', age = '65')
my_users.add_user(name = 'Vovik', sur = 'Razumov', age = '36')

my_users.print_users()
print()
my_users.print_sorted()
