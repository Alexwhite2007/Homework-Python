class Rectangle:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def get_area_rectangle(self):
        return self.a * self.b

class Square:
    def __init__(self, side):
        self.side = side
    def get_area_square(self):
        return self.side**2

class Circle:
    def __init__(self, rad):
        self.rad = rad
    def get_area_circle(self):
        return self.rad**2 * 3.14
