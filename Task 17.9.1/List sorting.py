# функция сортировки
def list_sort(array_list):
    for i in range(len(array_list)):  # бежим циклом по массиву
        idx_min = i  # сохраняем индекс предположительно минимального элемента
        for j in range(i, len(array_list)):
            if array_list[j] < array_list[idx_min]:
                idx_min = j
        if i != idx_min:  # если индекс не совпадает с минимальным, меняем
            array_list[i], array_list[idx_min] = array_list[idx_min], array_list[i]
    return array_list

# функция бинарного поиска
def bi_search(any_num: int, array_list: list) -> int:
    left, right = 0, len(array_list)   # левая граница от 0 до правая граница - длина массива
    while left < right:
        middle = (left + right) // 2  # определяем значение середины
        if array_list[middle] < any_num:   # если середина массива меньше введенного числа
            left = middle + 1  # присваиваем левой границе значение середина + 1
        else:
            right = middle  # присваиваем правой границе значение середины
    return left

# тело программы
Data = True
while Data:
        try:
            array = input("Введите последовательность чисел через пробел: ")
            any_num = int(input("Введите любое целое число для его поиска в массиве: "))
            array_list = [int(i) for i in array.split()]
            print("Список введенных чисел до сортировки:", array_list)
            print("Список после сортировки по возрастанию:", list_sort(array_list))

            # поиск введенного числа в массиве и его позиции
            if any_num in array_list:
                num_index = bi_search(any_num, array_list)
                print("Индекс первого искомого числа в отсортированном массиве: ", num_index)
                if num_index == 0:
                    print(f'Число {any_num} - первое значение в списке, следующее = {array_list[num_index+1]}')
                elif num_index == int(len(array_list)-1):
                    print(f'Число {any_num} - последнее значение в списке, предыдущее значение {array_list[num_index-1]}')
                else:
                    print(f'Предыдущее значение {array_list[num_index-1]}, следующее {array_list[num_index+1]}')

            else:
                print(f'Введенное число {any_num} отсутствует среди чисел массива')

        except ValueError:
            print(f'Ошибка ввода {ValueError}')
            print('Введено недопустимое значение.')
            Data = input("Повторить ввод данных? (Введите + или -): ")
        if Data != '+':
            print('Программа закончена.')
            Data = False
            exit()
