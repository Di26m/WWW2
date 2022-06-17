# ------------Работа с файлами---------
# data = input ("Введите текст:  ")
#
# file = open('data/text.txt', 'a')# w -запись перезапись, а - запись с добавлением информации
#
#
# file.write(data + "\n")
#
# file.close()
# -----------считвыание данных -----------
file = open('data/text.txt', 'r')

# print(file.read())
for line in file:
    print(line, end="")

file.close()
