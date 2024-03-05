# ООП - Объектно Ориентрованное Программирование
# DRY - Don`t Repeat Yuorself == не повторяй себя

class Car: # чертеж или же шаблон
    wheels = 4 # Атрибут\свойства\поле класса
    # __init__ - конструктор
    # self - сам объект
    def __init__(self, model, year, color):
        self.model = model # Атрибут\поле\свойства объекта
        self.year = year
        self.color = color
        self.is_start = False
        self.tank = 0

    def info(self):
        print(f"модель - {self.model}, \nгод выпуска - {self.year}, \nцвет - {self.color}, \nмашина зведена? {self.is_start}")

    def start(self):
        self.is_start = True
        print("Машина завелась")

    def drive(self, city):
        if self.is_start == True and self.tank >= 10:
            print(f"Машина едет {city}")
        else:
            print("Заведите машину")

    def broken(self):
        self.is_start = False
        print("Машина сломалась")

    def stop(self):
        self.is_start = False
        print("Машина заглушена")





mers_1 = Car("mers", 1992, "Black")
mers_2 = Car("mers - cls", 1999, "White")
# mers - объект класса (экземпляр класса)
bmw = Car("bmw - x7", 2018, "White")
mers_1.info()
mers_1.start()
# mers_1.broken()
mers_1.drive("Osh")
mers_1.stop()
# audi = Car()
# print(mers.model)
# print(mers.model, mers.color, mers.year)
# print(bmw.model, bmw.color, bmw.year)

