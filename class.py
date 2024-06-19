# classes and objects

# implementing classes and objects from UML designs
# static variables can be accessed by all objects and are constant
#you access them using the class name
# instance variables are peculiar to each instance so we use self
# self deals with the instance of the class.
# https://favtutor.com/blogs/static-variable-python


class Car:
    

    def __init__(self, make, model, year, max_speed) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed

        self.fuel_level = 100
        self.fuel_capacity = 100

    def drive_car(self):
        print('drive car')

    def stop_car(self):
        print('stop car')

    def add_fuel(self, new_fuel):
        
        if self.fuel_capacity >= 100:
            print('Fuel tank is at maximum capacity')
        else:
            new_fuel= 100 - self.fuel_capacity
            self.fuel_capacity = self.fuel_capacity + new_fuel
            print(self.fuel_capacity)
            print(f'Fuel tank has been refilled with {new_fuel}ghs worth of fuel')

car1 = Car("bmw","5-series", 2017, 250)
car1.fuel_capacity = 75
car1.add_fuel(40)