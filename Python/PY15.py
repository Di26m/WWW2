# ----------With as-----------
# file = open('text2.txt', 'r')
# file.read()
# file.close()
# ----------------
# try:
#     file = open('text2.txt', 'r')
#     file.read()
#
# except FileNotFoundError:
#     print(" Файл не найден")
# finally:
#     file.close()
# -------------------------
try:
    with open('data/text2.txt', 'r', encoding='utf-8') as file: # with as - самостоятельно открывает и закрывает файл
        print(file.read())

except FileNotFoundError:
    print(" Файл не найден")