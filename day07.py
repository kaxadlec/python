import math


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        print('도형의 면적을 출력합니다')


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, x, y, width, length):
        super().__init__(x, y)
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length

    def __repr__(self):
        return f'사각형의 좌표는 x:{self.x}, y:{self.y}이고 넓이는 {self.get_area()}'

    def __add__(self, other):
        return (self.width * self.length) + (other.width * other.length)  # 두 사각형의 합
        # return Rectangle(0, 0, (self.width + other.width), (self.length + other.length))


c1 = Circle(100, 100, 10.2)  # c1 객체
c2 = Circle(100, 100, 2.3)
r1 = Rectangle(100, 100, 2, 3)
r2 = Rectangle(2, 2, 10, 30)

# print(c1.get_area())
# print(c2.get_area())
# print(f'사각형의 좌표는 x:{r1.x}, y:{r1.y}이고 넓이는 {r1.get_area()}')
print(r1)
print(r2)
print(r1 + r2)


class Cylinder(Circle):
    def __init__(self, x, y, radius, height):
        super().__init__(x, y, radius)
        self.height = height

    def get_area(self):
        # return math.pi * self.radius * self.radius * self.height    # 밑과 동일
        return super().get_area() * self.height


cy1 = Cylinder(20, 20, 5, 2)
print(f'\n원기둥의 부피는 {cy1.get_area()}')

