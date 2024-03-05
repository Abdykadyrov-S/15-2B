#  Инкапсуляция

class SmartPhone:
    def __init__(self, model, battery, sim_cards):
        self.model = model # Публичное
        self._battery = battery # Защищенное
        self.__sim_cards = sim_cards # Приватное

    @property
    def sim_cards(self):
        return self.__sim_cards

    def info(self):
        print(f"модель телефона - {self.model}, {self._battery}, {self.__sim_cards}")
        self._protection()

    def _protection(self):
        print("protection info")

    def __password(self):
        print("012345678")

    @property
    def password(self):
        return self.__password

# phone = SmartPhone("Iphone 14 pro", 100, "Mega")
# phone.info()
# phone.password()



# print(phone.sim_cards)
# print(phone._battery)
# print(phone.__sim_cards)



# @ - декоратор
    
def lux(func):
    def cats():
        print("HI, спасибо что используете наш декоратор")
        func()
        print("Bye!")

    return cats



# @lux
def add():
    print(2 + 2)

add()


