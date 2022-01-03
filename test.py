text = input('введите строку: ')

lower = upper = 0
for sym in text:
    if sym.islower():
        lower += 1
    elif sym.isupper():
        upper += 1

if lower > upper:
    print(text.lower())
else:
    print(text.upper())
