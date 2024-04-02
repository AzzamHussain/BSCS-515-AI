import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

def calculate_area(shape):
    return shape.area()

# Create instances of different shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4)

# Call area calculation function on each shape
print("Circle area:", calculate_area(circle))       # Output: Circle area: 78.53981633974483
print("Rectangle area:", calculate_area(rectangle)) # Output: Rectangle area: 24
print("Triangle area:", calculate_area(triangle))   # Output: Triangle area: 6.0
