class Rectangle:
    def __init__(self, width, heigth, color):
        self.width = width
        self.heigth = heigth
        self.color = color

    def __str__(self):
        return f'Атрибуты прямоугольника :\nширина {self.width},\nвысота {self.heigth},\nцвет - {self.color}.'


rect_1 = Rectangle(5, 10, 'красный')
print(rect_1)