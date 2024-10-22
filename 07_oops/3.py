# Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class 
# and has an additional attribute battery_size.

# Class method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

class Car:
    # below one is the constructor
    def __init__(self, brand, model):     # self is like 'this' keyword
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


# now lets make new class
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size 


my_tesla = ElectricCar("Tesla", "Model s", "85kwh")
print(my_tesla.battery_size)
print(my_tesla.full_name())


my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)