#OOP Exercise 10: Calculate the area of different shapes using OOP

class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1415*self.radius*self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side*self.side

# Example of polymorphism
shapes = [Circle(5), Square(7), Circle(3)]

for shape in shapes:
    print(shape.area())  # Output: 78.53975, 49, 28.27431