# ______________Функции (def, lamda__________)
# def test_func(word):
#     print(word, end='')
#     print('!')
#
# test_func('Hi')
# test_func(5)
# -------------
# def summa(a, b):
#     return a + b
#
# res = summa(5.5, 7.5)
# print(res)
# print(summa('H', 'i'))
# -----------------------функция выбора минимального числа из 2 х массивов(списков)
# def minimal(l):
#     min_num = l[0]
#     for el in l:
#         if el < min_num:
#             min_num = el
#     return min_num
#
nums1 = [5, 7, 2, 9, 4, -10]
# min1 = minimal(nums1)
#
nums2 = [5, 7, 2.1, 9.4, 4, -4, ]
# min2 = minimal(nums2)
#
# if min1 < min2:
#     print(min1)
# else:
#     print(min2)
# # ------Сам придумал)------- надо доработать с retern и объединением массивов
# def minimal2(b):
#     b.sort()
#     print(b[0])
#
# minimal2(nums1)
# minimal2(nums2)
# ____________lambda анонимные функции-------------
func1 = lambda x, y: x * y
print(func1(5, 2))
# ------Сам придумал 2)------- то что с retern хотел сделать, минимальное число из 2 х массивов через lambda
func2 = lambda nums1, nums2: nums1.extend(nums2)
nums1.sort()
print(nums1[0])
