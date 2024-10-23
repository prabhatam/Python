# Class inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.


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




# now lets make new class
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size 
    
    def fuel_type(self):
        return "Electric charge"


my_tesla = ElectricCar("Tesla", "Model s", "85kwh")
print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))

# print(my_tesla.battery_size)
# print(my_tesla.brand)
# print(my_tesla.get_brand())
# print(my_tesla.model)
# print(my_tesla.full_name())
# print(my_tesla.fuel_type())


# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())


# my_new_car = Car("Tata", "Safari")
# safariThree = Car("Tata", "Nexon")
# print(safariThree.total_car)
# or
# print(Car.total_car)


# lets try to overwrite the model name
# my_new_car.model = "City" # this line is giving us error => we can't overwrite
# print(my_new_car.model) # this is accessing the model method but due to property decorator we can use that as attribute
# we are able to overwrite the model name but we want only to read 
# => firstly make model private then make a static method to read only



# print(my_new_car.fuel_type())

# print(Car.general_description())