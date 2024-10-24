import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = []
        self.filled = False
        self.set_color(*color)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self, *sides):
        perim_f = 0
        for side in self.__sides:
            perim_f += side
        return perim_f

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) is True:
            self.__sides = [*new_sides]
        else:
            pass


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, side):
        super().__init__(color, side)
        self.set_sides(side)
        super().set_color(*color)
        self.__radius = side / 2

    def get_square(self):
        c_square = math.pi * self.__radius ** 2
        return c_square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, side_a, side_b, side_c):
        super().__init__(color, side_a, side_b, side_c)
        self.set_sides(side_a, side_b, side_c)
        super().set_color(*color)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_square(self):
        tr_h_p = self.__len__() / 2  # полупериметр треугольника
        tr_square = math.sqrt(tr_h_p *
                              (tr_h_p - self.side_a) *
                              (tr_h_p - self.side_b) *
                              (tr_h_p - self.side_c))
        return tr_square


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        super().__init__(color, side)
        self.set_sides(*(side for i in range(self.sides_count)))
        super().set_color(*color)

    def get_volume(self):
        cube_sq = self.get_sides()[0] ** 3
        return cube_sq


if __name__ == '__main__':
    # Пример кода для проверки
    circle1 = Circle((200, 200, 100), 10)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())  # [55, 66, 77]
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())  # [222, 35, 130]

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())  # [15]

    # Проверка периметра (круга):
    print(len(circle1))  # 15 (периметр для круга воспринимаем как длину окружности)

    # Проверка объёма (куба):
    print(cube1.get_volume())  # 216 (6^3)
