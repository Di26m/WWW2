# ------Наследование, ИнкапсуляцияБ Полиморфизм-------
class Building:
    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year:", self.year, ". City:", self.city)

class School(Building): # Новый класс School наследует все от класса Building
    pupils = 0
    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city) #Super - вызывает класс родитель.  School -класс через котрый мы все
        # вызываем. Передаем параметр self. __init__  - обращаемся к родительскому конструктору. (  , ) - указываю,
        # что передаю
        self.puils = pupils

    def get_info(self): #  - Тут полиморфизм. Обращаемся к родительскому классу и добавляем печать pupils
        super().get_info()
        print("Pupils:", self.puils)



class House(Building):
    pass

class Shop(Building):
    pass
school = School(100, 2000, 'Moscow')
school.get_info() # Запускаем get_info для объекта school

house = House(2001, 'Moscow')
house.get_info()
shop = Shop(2002, 'Moscow')
shop.get_info()