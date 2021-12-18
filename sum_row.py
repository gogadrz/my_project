# Введите точность: 0.001
# Введите number: 4
# Сумма ряда =  0.2836250150891709
# number = 4
# precision = 0.001
import math

def toExp(number, multiplicity):
    summ = number
    for i in range(2, multiplicity + 1):
        if summ == 0:
            summ = number * number
        else:
            summ = summ * number
    return summ

def toFact(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:

        factor = 2
        summ = 0

        for i in range(3, n + 1):
            factor *= i
            summ = factor
        return summ

x = 5
i = 2
cnt = 5
cnt2 = cnt
print('x =', x)
value = 1
value2 = value

while cnt > 0:
    cnt -= 1
    value += (toExp(x, i) / toFact(i)) * -1

    value2 += x ** i / math.factorial(i) * -1

    print(1 + value * -1, '\t', 1 + value2 * -1)
    i += 2
