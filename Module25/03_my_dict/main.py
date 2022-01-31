class MyDict(dict):

    def get(self, *args):
        if len(args) == 1:
            return super(MyDict, self).get(args[0], 0)
        else:
            return super(MyDict, self).get(*args)


some_dict = MyDict()
some_dict['car'] = 'vaz'

print(some_dict)

print('Вызов get по умолчанию: {}'.format(some_dict.get('bike')))
print('Вызов со вторым параметром : {}'.format(some_dict.get('bike', 'no')))
