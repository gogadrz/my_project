friends_accounts = []

friends = int(input('Кол - во друзей: '))
for _ in range(friends):
    friends_accounts.append(0)

receipt = int(input('Долговых расписок: '))

for i_receipt in range(1, receipt + 1):
    print('\n', i_receipt, ' расписка', sep='')
    to_friend = int(input('Кому: '))
    from_friend = int(input('От кого: '))
    how_money = int(input('Сколько: '))

    balans = friends_accounts[to_friend - 1]
    balans -= how_money
    friends_accounts[to_friend -1] = balans

    balans = friends_accounts[from_friend - 1]
    balans += how_money
    friends_accounts[from_friend - 1] = balans

print('\nБаланс друзей:')
for i_friend in range(1, friends + 1):
    print(i_friend, ': ', friends_accounts[i_friend - 1], sep='')


