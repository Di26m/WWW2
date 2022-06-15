# ____________Кортежи----------
# data = (4, 6, 7, 3, 6, True, 5.6, 'Hello')

# print(data[1:5])
# print(data.count(6))
# print(len(data))
# ------------------
# data = 5, 7, True
# data = (5,)
# print(data)
# -----------------
data = (4, 6, 7, 3, 6, True, 5.6, 'Hello')
for el in data:
    print(el)

nums = [5, 7, 8]

new_data = tuple(nums) # Преобразование списка в кортеж
word = tuple('Hello world') # Преобразование строки в кортеж
print(new_data)
print(word)