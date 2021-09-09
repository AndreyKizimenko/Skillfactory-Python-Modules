tickets_number = int(input('Количество билетов = '))
age = [int(input('Возраст  = ')) for num in range(tickets_number)]
price = 0

for num in age:
    if num < 18:
        continue
    elif 18 <= num < 25:
        price += 990
    else:
        price += 1390

if tickets_number > 3:
    print(f'Итоговая цена со скидкой 10% = {int(price * 0.9)}')
else:
    print(f'Итоговая цена = {price}')