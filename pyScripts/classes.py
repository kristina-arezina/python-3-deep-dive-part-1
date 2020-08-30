class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
r1 = Rectangle(10, 20)

r1.width

r1.width = 100

r1.width

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

print(str(r1))

print(hex(id(r1)))
