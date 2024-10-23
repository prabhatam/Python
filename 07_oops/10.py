# Multiple Inheritance
# Problem: Create two classes Battery and Engine, and 
# let the ElectricCar class inherit from both, demonstrating multiple inheritance.


class Car:
    total_car = 0     # defined a class variable

    # below one is the constructor
    def __init__(self, brand, model):     # self is like 'this' keyword
        self.__brand = brand              # by putting 2 underscore before the variable, makes it a private variable
        self.__model = model
        Car.total_car +=1

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    # static method are decorators, used to enhance the functionality of methods
    @staticmethod # this makes the method static
    def general_description():      
        # when the method is static, we don't need to take 'self' bcz self is used when we are accesing using object
        return "Cars are means of transport"

    @property         # decorator
    def model(self):
        return self.__model



class Battery:
    def battery_info(self):
        return "this is battery"



class Engine:
    def engine_info(self):
        return "This is engine"


# multiple inheritance executing
class ElectricCar(Battery, Engine, Car):
    pass


my_new_tesla = ElectricCar("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
