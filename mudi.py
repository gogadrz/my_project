bon = 11


def f():
    bon = 3
    print('1 inside f()', bon)

    def d():
        # print('inside d()', bon)
        nonlocal bon
        bon = 5
    d()

    print('2 inside f()', bon)


f()
