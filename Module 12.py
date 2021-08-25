per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
list_values = list(per_cent.values())
money = int(input("Вклад – "))

deposit = [money * list_values[0] / 100 , money * list_values[1] / 100 , money * list_values[2] / 100 , money * list_values[3] / 100 ]
deposit_int = list(map(int,deposit))

print(deposit_int)
print(f'Максимальная сумма, которую вы можете заработать — {max(deposit_int)}')