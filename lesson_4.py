# Магические методы - dunder (double underscore) - окружены 2 нижними подчеркиваниями

"""В Python мы не вызываем эти методы вручную, это происходит автоматически"""

class Food:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight

    # def info(self):
    #     print(f"цена - {self.price} , вес в граммах - {self.weight}")

    def __str__(self): # __str__ == print
        return f"цена - {self.price} , вес в граммах - {self.weight}"
        # return "Hello World!"
    
    def __repr__(self): # __repr__ == print
        return f"цена - {self.price} , вес в граммах - {self.weight} это repr"
    
    def __call__(self, a, b): # Метод __call__ автоматически вызывается, когда к объекту обращаются как к функции
        print(a + b)

    # Магические методы для арифметических действий
        
    def __add__(self, other): # +
        print("Hello world")
    
    def __sub__(self, other): # -
        new_price = self.price - other.price
        new_weight = self.weight - other.weight
        return Food(new_price, new_weight)
    
    
    def __mul__(self, other): # *
        new_price = self.price * other.price
        new_weight = self.weight * other.weight
        return Food(new_price, new_weight)
    
    def __truediv__(self, other): # /
        new_price = self.price / other.price
        new_weight = self.weight / other.weight
        return Food(new_price, new_weight)
    
    def __floordiv__(self, other): # //
        new_price = self.price // other.price
        new_weight = self.weight // other.weight
        return Food(new_price, new_weight)
    
    def __eq__(self, other):
        return self.price == other.price

pizza = Food(400, 500) # вызывается __init__ 
hamburger = Food(60, 150) # вызывается __init__ 
# print(pizza.price, pizza.weight)

print(pizza)  # __str__

pizza(2, 8) # __call__

# Магические методы для арифметических действий
print(pizza + hamburger)
print(pizza - hamburger)
print(pizza * hamburger)
print(pizza / hamburger)
print(pizza // hamburger)


print(pizza == hamburger)

