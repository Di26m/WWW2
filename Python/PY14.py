# --------Обработчик исключений. Конструкция try - except----------

# x = 0
# while x == 0:
#     try:
#         x = int(input(" Введите число:  "))
#         x += 5
#         print(x)
#     except ValueError:
#         print(" Введите лучше число")
try:
    x = 5/ 1
    x = int(input(" Введите число:  "))
except ZeroDivisionError:
    print(" На ноль не делят !")
except ValueError:
    print(" Вы ввели что то не так")
else:
    print("else")
finally:
    print("Final")