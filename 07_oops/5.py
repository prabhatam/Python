# Polymorphism :- anek roop dharan kar sakta hai
# Problem: Determine polymorphism by defining a method fuel_type in 
# both Car and ElectricCar classes, but with different behaviours.


class Car:
    # below one is the constructor
    def __init__(self, brand, model):     # self is like 'this' keyword
        self.__brand = brand              # by putting 2 underscore before the variable, makes it a private variable
        self.model = model

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "Petrol or Diesel"


# now lets make new class
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size 
    
    def fuel_type(self):
        return "Electric charge"


my_tesla = ElectricCar("Tesla", "Model s", "85kwh")
# print(my_tesla.battery_size)
# print(my_tesla.brand)
# print(my_tesla.get_brand())
# print(my_tesla.model)
# print(my_tesla.full_name())
print(my_tesla.fuel_type())


# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())


my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)
print(my_new_car.fuel_type())