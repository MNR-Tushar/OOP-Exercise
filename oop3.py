#OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

varsity_bus=Bus("YKSG-2",200,10)
print(f"Vehicle name: {varsity_bus.name} Volvo speed: {varsity_bus.max_speed} Mileage: {varsity_bus.mileage}")