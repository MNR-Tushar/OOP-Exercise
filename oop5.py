#OOP Exercise 5: Define a property that must have the same value for every class instance (object)

class Vehicle:

    color="whitle"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display(self):
        return f"Colors: {self.color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}"


class Bus(Vehicle):

    
   pass

class Car(Vehicle):

    
    pass
    

varsity_bus=Bus("School Volvo",180,12)
print(varsity_bus.display())

all_car=Car("Audi Q5", 240,18)
print(all_car.display())