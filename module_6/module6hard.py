class Figure:
    filled = bool()

    def __init__(self, color, sides):
        self.__sides = sides
        self.__color = list(color)
        self.sides_count = 0
        self.set_sides(sides)

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def set_color(self, r, g, b):
        def __is_valid_color(red, green, blue):
            if isinstance(red, int) and isinstance(green, int) and isinstance(blue, int):
                if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:
                    return red, green, blue
                else:
                    return False

        if __is_valid_color(r, g, b) is False:
            pass
        else:
            self.__color = [r, g, b]
        return self.__color

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        def __is_valid_sides(*sides):
            for elem in range(len(sides)):
                for _side in range(len(sides[elem])):
                    if isinstance(sides[elem][_side], int) and sides[elem][_side] > 0:
                        return True
                    else:
                        return False

        if __is_valid_sides(new_sides) is True:
            if self.sides_count == len(new_sides):
                self.__sides = []
                for side in range(len(new_sides)):
                    self.__sides.append(new_sides[side])
                return self.__sides


class Circle(Figure):
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = sides
        self.sides_count = 1
        self.__radius = self.__sides // 3.14

    def get_square(self):
        return self.__radius ** 2 * 3.14

    def __len__(self):
        return self.__sides


class Triangle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__sides = list(sides)
        self.sides_count = 3
        self.__semiP = (self.__sides[0] + self.__sides[1] + self.__sides[2]) / 2
        self.__height = (2 * (self.__semiP * ((self.__semiP - self.__sides[0]) * (self.__semiP - self.__sides[1]) *
                                              (self.__semiP - self.__sides[0]) ** 0.5))) / self.__sides[0]

    def get_square(self):
        square = self.__height * self.__sides[0] * 0.5
        return "{:.2f}".format(square)


class Cube(Figure):
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.sides_count = 1
        self.__sides = [sides, sides, sides, sides, sides, sides, sides, sides, sides, sides, sides, sides]

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
