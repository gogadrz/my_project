# Введите первый год: 1900
# Введите второй год: 2100
#
# Года от 1900 до 2100 с тремя одинаковыми цифрами:
# 1911
# 1999
# 2000
# 2022

def print_year(num1, num2, num3, num4):
    print(num1, num2, num3, num4, sep = '')

start_year = int(input('Введите первый год: '))
end_year = int(input('Введите второй год: '))
print('\nГода от', start_year, 'до', end_year, 'с тремя одинаковыми цифрами:')

for year in range(start_year, end_year + 1):
    dig1 = year // 1000
    dig2 = year // 100 % 10
    dig3 = year // 10 % 10
    dig4 = year % 10

    if (dig1 == dig2 == dig3) or (dig1 == dig2 == dig4) or (dig1 == dig3 == dig4) or (dig2 == dig3 == dig4):
        print_year(dig1, dig2, dig3, dig4)

