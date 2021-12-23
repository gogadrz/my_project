goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]

print(goods)

fruit_name = input('Название фрукта: ')
fruit_price = int(input('цена: '))
fr = [fruit_name, fruit_price]

goods.append(fr)
print(goods)

for i_goods in goods:
    i_goods[1] += [i_goods][1] * .08

print(goods)
