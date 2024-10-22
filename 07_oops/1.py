# Basic Class and Object
# Problem: Create a car class with attributes like brand and model. Then create an instance of this class.

class Car:
    # below one is the constructor
    def __init__(self, brand, model):     # self is like 'this' keyword
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"


my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)