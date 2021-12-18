def aPayCalculate(credit, percent, years):
    return round((percent * (1 + percent) ** years) / ((1 + percent) ** years - 1) * credit, 2)

def printPeriod(summ, percent, aPayment, period):
    for i in range(1, period + 1):
        paidPercent = summ * percent
        paidCredit = aPayment - paidPercent
        print('\nПериод', i)
        print('\nОстаток долга на начало периода:', summ)
        print('Выплачено процентов:', paidPercent)
        print('Выплачено тела кредита:', paidCredit)
        summ -= paidCredit
    else:
        print('\nОстаток долга:', summ)
    return summ

credit = float(input('Введите сумму кредита: '))
years = int(input('На сколько лет выдан? '))
percent = int(input('Сколько процентов годовых? '))
percent /= 100
period = 3

aPay = aPayCalculate(credit, percent, years)
balance = printPeriod(credit, percent, aPay, period)
period = years - period
print('\n' + '=' * 50)
years = int(input('\nНа сколько лет продляется договор?: '))
period += years
percent = int(input('Увеличение ставки до: '))
percent /= 100
aPay = aPayCalculate(balance, percent, period)
printPeriod(balance, percent, aPay, period)

