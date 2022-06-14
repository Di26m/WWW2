# for i in range(1, 6, 2):
#     print(i)

# count = 0
# word = 'Hello World!'
# for i in word:
#     if i == "l":
#         count += 1
# print(count)
# -----------------------
# i = 5
# while i <= 15:   # до тех пор
#     print(i)
#     i += 2
# ------------------------
# isHasCar = True
#
# while isHasCar:
#     if input('Enter data:  ') == 'Stop':
#         isHasCar = False
# ------------------------
# for i in range(1, 11):
#     if i >= 5:
#         break
#     if i % 2 == 0:
#         continue
#     print(i)
# -------------------------
found = None
for i in 'hello':
    if i == 'l':
        found = True
        break
else:
    found = False
print(found)