def get_new_price(percent, price):
    if percent == 0:
        return price
    else:
        return round(price * (1 + percent / 100), 2)


price_list = [1.09, 23.56, 57.84, 4.56, 6.78]
first_year_percent = 0
second_year_percent = 10

first_year_prices = [get_new_price(first_year_percent, price) for price in price_list]
second_year_prices = [get_new_price(second_year_percent, price) for price in first_year_prices]

print(first_year_prices)
print(second_year_prices)
print(round(sum(price_list), 2), round(sum(first_year_prices), 2), round(sum(second_year_prices), 2))







# Сумма цен за каждый год: 93.83 93.83 103.22
