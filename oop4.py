#OOP Exercise 4: Class Inheritance

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    

class Bus(Vehicle):

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


varsity_bus=Bus("YKSG-2",200,10)
print(varsity_bus.seating_capacity(60))