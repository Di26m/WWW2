# -----------Конструкторы----------
# class Cat:
#     name = None
#     age = None
#     isHappy = None
#
#     def __init__(self, name, age, isHappy):
#
#         self.set_data(name, age, isHappy)
#
#         # get_data() - метод
#         self.get_data()
#     def set_data(self, name, age, isHappy):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#     def get_data(self):
#         print(self.name, "age:", self.age, ". Happy:", self.isHappy)
#
# cat1 = Cat("Барсик", 3, True)
# cat2 = Cat("Жопен", 2, False)
# --------------Переопределение методов--------------
class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name= None, age= None, isHappy= None):

        self.set_data(name, age, isHappy)

        # get_data() - метод
        self.get_data()
    def set_data(self, name = None, age = None, isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy
    def get_data(self):
        print(self.name, "age:", self.age, ". Happy:", self.isHappy)

cat1 = Cat()

cat1.set_data("John")

cat2 = Cat("Жопен", 2, False)