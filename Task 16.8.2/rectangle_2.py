from rectangle import Rectangle, Square, Circle

# создаем экземпляры фигур каждого из классов (прямоугольник, квадрат, круг)
rect_1 = Rectangle (3,4)
rect_2 = Rectangle(12,5)
square_1 = Square(5)
square_2 = Square(10)
circle_1 = Circle(4)
circle_2 = Circle(8)

# Наша коллекция экземпляров фигур
figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2] #составляем список из фигур (экземпляров классов)

for figure in figures:
    if isinstance(figure, Square): # если экземпляр класса - квадрат, то выводим его площадь.
        print(f'"Площадь квадрата равна: {figure.get_area_square()}')
    elif isinstance(figure, Circle): # если экземпляр класса - круг, то выводим его площадь.
        print(f'"Площадь круга равна: {figure.get_area_circle()}')
    else:
        print(f'"Площадь прямоугольника равна: {figure.get_area_rectangle()}') # в противном случае, экземпляр класса - прямоугольник, выводим его площадь.