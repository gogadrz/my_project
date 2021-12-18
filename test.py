# a = 1
# b = -3
# c = -12
# d = 10
import math

def sqrt2(number):
    if number < 0:
        number *= -1
        number = math.sqrt(number)
        number *= -1
        return number
    else:
        return math.sqrt(number)

a, b, c, d = 1, -3, 3, -1
print(a, b, c, d)
discr0 = (b) ** 2 - 3 * (a) * (c)
discr1 = 2 * (b) ** 3 + (- 9) * (a) * (b) * (c) + 27 * (a) ** 2 * (d)
discr = (discr1 ** 2 - 4 * discr0 ** 3) / 27 * a ** 2

# if discr > 0 три корня
#     если 0 два корня
# если < 0 один корень
# мда... мудрить тут и мудрить

CC = (math.sqrt((discr1 ** 2 - 4 * discr0 ** 3) * discr1 / 2)) ** (1. / 3.)
u = (-a * math.sqrt(-3)) / 2

n = 3   # 1, 2 или 3
value = -(b * u ** n * CC * discr0 / (u ** n * CC)) / 3 * a

print('d0 =', discr0, 'd1 =', discr1, 'd =', discr, 'C = ', CC, 'u =', u)
print('n =', n, ', value =', value)
