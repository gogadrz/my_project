class Family:
    name = 'Common family'
    fund = 100000
    having_a_house = False

    def show_info(self):
        print('Family name: {}, fund: {}, having a house: {}'.format(
            self.name, self.fund, self.having_a_house
        ))

    def to_earn_money(self, money):
        self.fund += money
        print('The family fund is replenished by {} rubles. Total amount: {} rubles'.format(
            money, self.fund
        ))

    def buy_house(self, price, amount=0):
        if price <= self.fund:
            price -= price * amount / 100
            self.fund -= price
            self.having_a_house = True
        else:
            print('Not enough money to buy house')


my_family = Family()
my_family.show_info()

print('The family made money...')
my_family.to_earn_money(500000)

print('Try to buy a house')
my_family.buy_house(10000000)
my_family.show_info()

print('The family made money')
my_family.to_earn_money(400000)

my_family.buy_house(1000000, 5)
my_family.show_info()

