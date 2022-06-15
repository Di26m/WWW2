# nums = [5, 7, 10, 2, 4, True, 'Hello', 6.7, [5, 7]] # массив
#
# nums[0] = 50 # индексы массива
# nums[5] = 1.01
#
# print(nums[-1][1])
# --------------------
# numbers = [5, 2, 7]
# numbers.append(100) # добавить элемент в список
# numbers.insert(1, True) # добавление элемента перед 1
#
# b = [5, 6, 8]
# numbers.extend(b) # добавить список в конец списка
# numbers.sort() # сорировка по порядку
# # numbers.reverse() # сорировка по с конца
# numbers.pop() # удаляет последний элемент списка или по индексу
# numbers.remove(True) # Удаляет элемент списка по значению
# # numbers.clear() # Удалить все элементы списка
#
# # print(numbers.count(5)) # Подсчет элементов по значению
# print(len(numbers)) # Подсчет кол ва элементов в списке
# ---------------------------------
# nums = [5, 2, 7, '50', False]
#
# for el in nums: # Вывод списка через цикл
#     el *= 2
#     print(el)
# ----------------------------------
n = int(input("Enter length: ")) # вводим длину списка
user_list = []
i = 0
while i < n: # Пока i < n вводим значения и добавляем их в список
    string = 'Enter element #' + str(i+1) + ': '
    user_list.append(input(string))
    i += 1
print(user_list)