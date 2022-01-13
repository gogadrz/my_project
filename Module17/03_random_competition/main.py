import random


def main():
    members_cnt = 20
    first_team = [round(random.uniform(5, 10), 2) for _ in range(members_cnt)]
    second_team = [round(random.uniform(5, 10), 2) for _ in range(members_cnt)]
    winners_list = []

    for i_member in range(members_cnt):
        if first_team[i_member] > second_team[i_member]:
            winners_list.append(first_team[i_member])
        else:
            winners_list.append(second_team[i_member])

    print('Первая команда:', first_team)
    print('Вторая команда:', second_team)
    print('Победители тура:', winners_list)


if __name__ == '__main__':
    main()
