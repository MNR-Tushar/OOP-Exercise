class Vehicle:
    
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage

car =Vehicle(300,15)
print(car.max_speed,car.mileage)
