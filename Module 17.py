# Функция сравнения элемента с текущим индексом и предшествующим
def search(array, element, left, right):
    if element > array[right-1]:
        print('Ваше число выше всех чисел последовательности')
        return
    elif element < array[left]:
        print('Ваше число меньше всех чисел последовательности')
        return

    mid = (left + right) // 2

    while True:
        # Совпадает ли элемент с центральным и больше ли он предыдущего
        if array[mid] == element and element > array[mid-1]:
            print(f'Введенное число находится между {array[mid - 1]} и {array[mid]}')
            print(f'Индекс предшествующего числа : {mid - 1}')
            break
        # Проверка вправо
        elif array[mid] > element > array[mid - 1]:
            print(f'Введенное число находится между {array[mid - 1]} и {array[mid]}')
            print(f'Индекс предшествующего числа : {mid - 1}')
            break
        # Проверка влево
        elif array[mid] < element < array[mid - 1]:
            print(f'Введенное число находится между {array[mid - 1]} и {array[mid]}')
            print(f'Индекс предшествующего числа : {mid - 1}')
            break
        # Если элемент меньше середины, то уменьшаем индекс и двигаемся влево
        elif element < array[mid]:
            mid -= 1
        # Если элемент выше середины, то увеличиваем индекс и двигаемся вправо
        else:
            mid += 1


# Функция сортировки списка по возрастанию
def sort_list(new_list):
    for i in range(1, len(new_list)):
        x = new_list[i]
        idx = i
        while idx > 0 and new_list[idx - 1] > x:
            new_list[idx] = new_list[idx - 1]
            idx -= 1
        new_list[idx] = x

    print(new_list)


# Запрашиваем и проверяем новый список у юзера
main_list = []

while len(main_list) < 2:
    try:
        main_list = list(map(int, input("Ввведите последовательность чисел через пробел ").split()))
    except:
        pass
print(main_list)

# Сортируем список
sort_list(main_list)

# Запрашиваем число
while True:
    try:
        user_choice = int(input('Введите число '))
    except:
        pass
    else:
        print(f'Вы ввели: {user_choice}')
        break


# Запускаем функцию для поиска индекса числа
search(main_list, user_choice, 0, len(main_list))

# Чтобы программа не закрывала сразу же терминал/консоль
input("Press enter to exit ;")