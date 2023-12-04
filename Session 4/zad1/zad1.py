import math

class Triangle:
    def __init__(self, a, base):
        if a <= 0 or base <= 0 or a + a <= base: #checking the relationship of base length to arm length
            raise ValueError('Invalid triangle dimensions.')
        self.a = a
        self.base = base
        self.h = math.sqrt(a**2 - (base/2)**2)

    def area(self):
        return round(self.base * self.h / 2, 2)

    def perimeter(self):
        return 2 * self.a + self.base

    def display_info(self):
        print('Triangle:')
        print(f'\tSide length: {self.a}')
        print(f'\tBase length: {self.base}')
        print(f'\tHeight: {self.h}')
        print(f'\tArea: {self.area()}')
        print(f'\tPerimeter: {self.perimeter()}')
        print('---')

class Circle:
    def __init__(self, r):
        if r < 0:
            raise ValueError('Radius must be non-negative.')
        self.r = r
        self.pi = math.pi

    def area(self):
        return round(self.pi * self.r**2, 2)

    def perimeter(self):
        return round(2 * self.pi * self.r, 2)

    def display_info(self):
        print('Circle:')
        print(f'\tRadius: {self.r}')
        print(f'\tArea: {self.area()}')
        print(f'\tPerimeter: {self.perimeter()}')
        print('---')

class Rectangle:
    def __init__(self, a, b):
        if a < 0 or b < 0:
            raise ValueError('Length and width must be non-negative.')
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * self.a + 2 * self.b

    def display_info(self):
        print('Rectangle:')
        print(f'\tLength: {self.a}')
        print(f'\tWidth: {self.b}')
        print(f'\tArea: {self.area()}')
        print(f'\tPerimeter: {self.perimeter()}')
        print('---')

def create_triangle():
    try:
        triangle1 = Triangle(5, 4)
        triangle1.display_info()
    except ValueError as e:
        print(f"Error creating Triangle: {e}")

def create_circle():
    try:
        circle1 = Circle(5)
        circle1.display_info()
    except ValueError as e:
        print(f"Error creating Circle: {e}")

def create_rectangle():
    try:
        rectangle1 = Rectangle(4, 1)
        rectangle1.display_info()
    except ValueError as e:
        print(f"Error creating Rectangle: {e}")

create_triangle()
create_circle()
create_rectangle()