# procedure oriented programming language

# aspacts of OOPs
# 1. encapsulation
# 2. inheritance
# 3. polymorphism
# 4. reusability
# 5. data hiding

# class and object
class Car:
    total_car = 0
    def __init__(self,userbrand, usermodel):
        self.__userbrand = userbrand
        self.__usermodel = usermodel
        Car.total_car += 1

    # encapsulation
    def get_brand(self):
        return self.__userbrand

    def full_name(self):
        return f"{self.__userbrand} {self.__usermodel}"
    
    # polymorphism
    def fuel_type(self):
        return "petrol & deisel"
    
    @staticmethod
    def general_description():
        return "car is heavy and fast"
    
    @property
    def usermodel(self):
        return self.__usermodel

# inheritance
class Electric(Car):
    def __init__(self, userbrand, usermodel, battery_size):
        super().__init__(userbrand, usermodel)
        self.battery_size = battery_size

    # polymorphism
    def fuel_type(self):
        return "Electric battery"


my_tesla = Electric("tesla", "model s", 75)
# print(my_tesla.full_name())
# print(my_tesla.get_brand())

my_car = Car("toyota", "innova")
# my_car.usermodel = "nano"
# print(my_car.userbrand)
# print(my_car.full_name())

# polymorphism
# print(my_tesla.fuel_type())
# print(my_car.fuel_type())
# print(Car.total_car)

# print(Car.general_description())

# print(my_car.usermodel)

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, Electric))

# inheritance
class Battary:
    def battery_info(self):
        return "battery"

class Engine:
    def engine_info(self):
        return "engine"

class ElectricCarTwo(Car, Battary, Engine):
    pass

new_tesla = ElectricCarTwo("tesla", "model s")
print(new_tesla.engine_info())
print(new_tesla.battery_info())