# Основные принципы ООП

# Наследование и Абстракция

class Person: # Родительский и Абстрактный класс
    def __init__(self, name, age, eyes):
        self.name = name
        self.age = age
        self.eyes = eyes

    def info(self):
        print(f"{self.name}, {self.age}, {self.eyes}")

    def run(self):
        print(f"{self.name} - бежит")

# human_1 = Person("Eliza", 16)
human_2 = Person("Luntik", 15, "purple")
human_2.info()


class Parents(Person): # Дочерний класс
    def __init__(self, name, age, eyes, child):
        # super().__init__(name, age, eyes)
        Person.__init__(self, name, age, eyes)
        self.child = child

    def info(self):
        print(f"{self.name}, {self.age}, {self.eyes}, {self.child}")

    def bring_up(self):
        print(f"этот - {self.name} присматривает за {self.child} - детьми")

parent_1 = Parents("Stif - Father", 65, "Blue", 4)
parent_1.info()
parent_1.run()
parent_1.bring_up()





class Transport: # Абстрактный класс
    def __init__(self, model, year, color):
        self.model = model # Атрибут\поле\свойства объекта
        self.year = year
        self.color = color

    def info(self):
        print(f"модель - {self.model}, \nгод выпуска - {self.year}, \nцвет - {self.color}, \nмашина зведена? {self.is_start}")

    def broken(self):
        print("Машина сломалась")

    def stop(self):
        print("Транспорт не движется")

