def test_fun(*args, **kwargs):
    for i in args:
        print(i)

    for key, value in kwargs.items():
        print(key, value)
    return


test_fun('1 аргумент', '2 аргумент', '3 аргумент', '4 аргумент',
         year=2022, hobby='diveing')
