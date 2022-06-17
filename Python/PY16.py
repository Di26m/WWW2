# # -----------Модули---------
# import datetime as d, sys, os, platform  # модуль дата время. (as) - присваивает псевдоним (d)
#
# from math import sqrt as s, ceil # импортируем из модуля (math) функцию (sqrt)  и обзываем ее (s)
# # import array # можуль для работы с массивами
# # import math # можуль для работы с математическими
# # print(d.datetime.now().time()) # - time - выводим текущее время, date - дата
# # print(sys.path) # выводит путь к файлу
# # print(os.name) # выводит имя операционной системы
# # print(platform.system()) # выводит имя операционной системы (рабочее название)
# print(ceil(s(25)))
# # --------Собственный модуль------
# # import mymodule as my
# #
# # print(my.name)
# # my.hello()
# # ------------
# from mymodule import add_three_numbers as th
# print(th(5, 3, 0))
# ---------------
import cowsay
cowsay.cow('Hello')