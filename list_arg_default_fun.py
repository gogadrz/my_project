def mud(number, lst=None):
    # if not lst:
    #     lst = []

    lst = lst or []
    lst.append(number)
    print(lst)
    return


mud(5, [1, 3, 5])
mud(10)
mud(15)

