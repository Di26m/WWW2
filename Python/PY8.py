# word = 'Football, basketTball, skate'
# # print(len(word)) # Подсчет количества символов
# # # print(word.count('r')) # подсчет символов R
# # print(word.upper()) # перевод строки в верхний регистр
# # print(word.isupper()) # True или False  если вся строка в верхнем или нижнем регистре
# # print(word.islower()) # True или False  если вся строка в верхнем или нижнем регистре
# # print(word.capitalize()) # Первая буква заглавная остальные в нижний регистр
# # print(word.find('p')) # Поиск символа, с указанием его места
# # print(word.split(', ')) # Разбивает строку по символу и делает из нее список
# hobby = word.split(', ')
# # print(hobby[1])
#
# for i in range(len(hobby)): # диапазон (range), до длины (len), списка (hobby), для каждого i списка, применяем capitalize
#     hobby[i] = hobby[i].capitalize()
# result = ', '.join(hobby) # собираем обратно строку по ', ' с помощью join
# print(result)
# -------------------------Индексы и срезы________________________
# word = 'Football'
#
# print(word[0:4]) # диапазон символов
# print(word[1:-1:2]) # диапазон символов с шагом
# -------------
lis = [6, 4, "Stroka", True, 6.5]
print(lis[2:5])
print(lis[::2]) # Весь диапазон с шагом (каждый второй)
print(lis[::-1]) # Весь диапазон с разворотом списка
