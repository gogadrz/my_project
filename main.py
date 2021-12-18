def period_printout(summ, percent, a_payment, period):
    for i in range(1, period + 1):
        paid_percent = summ * percent
        paid_credit = a_payment - paid_percent
        print('\nПериод', i)
        print('\nОстаток долга на начало периода:', summ)
        print('Выплачено процентов:', paid_percent)
        print('Выплачено тела кредита:', paid_credit)
        summ -= paid_credit
    else:
        print('\nОстаток долга:', summ)
    return summ
def payment(summ, year, percent):
    k = (percent * (1 + percent) ** year) / ((1 + percent) ** year - 1)
    a_payment = round(k * summ, 2)
    return a_payment
credit = float(input('\nВведите сумму кредита: '))
years = int(input('На сколько лет выдан: '))
percent_per_year = int(input('Сколько процентов годовых: '))
percent_per_year /= 100
period = 3
A = payment(credit, years, percent_per_year)
balance = period_printout(credit, percent_per_year, A, period)
period = years - period
print('\n' + '=' * 50)
years = int(input('\nНа сколько лет продляется договор?: '))
period += years
percent_per_year = int(input('Увеличение ставки до: '))
percent_per_year /= 100
A = payment(balance, period, percent_per_year)
period_printout(balance, percent_per_year, A, period)
# это рабочая версия исходника