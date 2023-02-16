
class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, value):
        if isinstance(value, int) and value > 0:
            self.__radius = value
        else:
            print('Wrong value for radius , it must be a positive number')

    def calculate_area(self):
        radius_2 = self.__radius * self.__radius
        return radius_2 * 3.14

    def info(self):
        return (f'Circle radius: {self.__radius}{Figure.unit}, '
                f'area: {i.calculate_area()}{Figure.unit}')


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def get_side_a(self):
        return self.__side_a

    def set_side_a(self, value):
        if isinstance(value, int) and value > 0:
            self.__side_a = value
        else:
            print('Wrong value for side A , it must be a positive number')

    def get_side_b(self):
        return self.__side_b

    def set_side_b(self, value):
        if isinstance(value, int) and value > 0:
            self.__side_b = value
        else:
            print('Wrong value for side B , it must be a positive number')

    def calculate_area(self):
        triangle = 0.5 * self.__side_a * self.__side_b
        return triangle

    def info(self):
        return(f'RightTriangle side a: {self.__side_a}{Figure.unit}, side b: {self.__side_b}{Figure.unit}, '
               f'area: {i.calculate_area()}{Figure.unit}.')


circle_1 = Circle(10)
circle_2 = Circle(5)
triangle_1 = RightTriangle(4, 5)
triangle_2 = RightTriangle(5, 6)
triangle_3 = RightTriangle(5, 8)


list_of_figures = [circle_1, circle_2, triangle_1, triangle_2, triangle_3]
for i in list_of_figures:
    print(i.info())





















