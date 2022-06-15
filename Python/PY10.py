# -----------Словари (dict)-----------
# country = {4: 3} # 4 - ключ к 3
# country = {(5, 6): 3} # кортеж - ключ к 3
# print(country[(5, 6)])
# -------------
# country = {'code': 'RU', 'name': 'Russian', 'population': 144}
# print(country['name'])
# ----------------Альтернативная запись словарей
# country = dict(code='RU', name='Russian')
# print(country['name'])
# --------------------------
# country = {'code': 'RU', 'name': 'Russian', 'population': 144}
# # print(country.items())
# for key, value in country.items():
#     print(key, ' - ', value)
# ---------------------------------
# country = {'code': 'RU', 'name': 'Russian', 'population': 144}
# # print(country.get('name')) # аналогично print(country['name'])
# # country.clear() # очистка словаря
# # country.pop('name') # удаление элемента по ключу
# # country.popitem() # удаление элемента последнего
# # print(country.keys) # Получение только ключей
# # print(country.values()) # получение только значений
# country['code'] = 'None' # обновление значений в словаре
# print(country.items()) # получение ключей и элементов в кортеже
# _________________________________________
person = {
    'user_1': {
        'first_name': 'John',
        'last_name': 'Marley',
        'age': 45,
        'address': ('г. Москва', 'улю Какая-то', '45'),
        'grades': {'math': 5, 'chemics': 3}
    },
    'user_2':
        {

        }
}
print(person['user_1']['address'])