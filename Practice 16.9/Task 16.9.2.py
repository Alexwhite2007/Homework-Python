class Rectangle:
    def __init__(self,  width, heigth):
        self.width = width
        self.heigth = heigth
    def get_area_rectangle(self):
        return self.width * self.heigth  #вернем площадь прямоугольника

# предлагаем ввести размеры прямоугольника:
width = int(input( "введите ширину прямоугольника = " ))
heigth = int(input( "введите высоту прямоугольника = " ))
rectangle = Rectangle(width, heigth) #применим класс
print(f'Площадь прямоугольника равна {rectangle.get_area_rectangle()}')