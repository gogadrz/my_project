def digital_root(n):
    return n % 9 or n or 0

    # m = n % 9
    # if m:
    #     return m
    # elif n:
    #     return 9
    # else:
    #     return 0


print(digital_root(123))
