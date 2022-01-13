passwd = input('Придумайте пароль: ')

if (len(passwd) < 8) or (sum(map(lambda x: x.isdigit(), passwd)) < 3) or (not any(sym.isupper() for sym in passwd)):
    print('Пароль ненадёжный. Попробуйте ещё раз.')
else:
    print('Это надёжный пароль!')
