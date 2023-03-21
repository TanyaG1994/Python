# Напишите программу, которой на вход подается последовательность чисел через пробел, а также запрашивается у
# пользователя любое число.
#
# В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии ввода данных.
#
# Далее программа работает по следующему алгоритму:
#
# 1.Преобразование введённой последовательности в список
#
# 2.Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
#
# 3.Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или
# равен этому числу.


def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
    return array


def binary_search(array, element, left, right):
    if left > right or left == len(array)-1:  # если левая граница превысила правую или левая граница равна наибольшему индексу
        return -1  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину последовательности
    if array[middle] < element and array[middle+1] >= element:
        return middle  
    elif element <= array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


pp = input('Введите последовательность целых чисел через пробел:' ) # pp - пользовательская последовательность

escape = 0 # условие выхода из цикла
set_1 = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '-'}
set_2 = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
while escape == 0: #проверяем формат введенной последовательности
    try:
        for i in range(0, len(pp)):
            if pp[i] not in set_1 or (pp[i] == '-' and (i == len(pp)-1 or pp[i+1] not in set_2)): #только положительные, отрицательные числа или пробел
                raise ValueError('Не верный формат ввода.')

    except ValueError as error:
        pp = input('Ошибка! Ведите только числа через пробел:')
    else:
        pp_list = list(map(int, pp.split()))
        escape = 1


pp_list_sort = qsort(pp_list, 0, len(pp_list)-1)
print('Последовательность отсортирована: ', pp_list_sort)

chislo = int(input('Введите число для поиска:' ))

result = binary_search(pp_list_sort, chislo, 0, len(pp_list_sort)-1)

if result >=0:
    print('Позиция искомого элемента в списке - ', result)
else:
    print('В списке нет элемента, соответствующего условию.')