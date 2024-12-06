class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = self.create_sides(*sides)
        self.__color = [0, 0, 0]
        self.filled = False
        self.set_color(*color)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            self.filled = True
        else:
            print("Неверный цвет")

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(side > 0 for side in sides)

    def create_sides(self, *sides):
        if len(sides) == self.sides_count:
            return list(sides)
        else:
            return [1] * self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        else:
            print("Неверное количество сторон")


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, radius)

    def get_square(self):
        return 3.14 * (radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, side1, side2, side3):
        super().__init__(color, side1, side2, side3)
        self.__sides = [side1, side2, side3]

    def get_square(self):
        a, b, c = self.__sides
        s = sum(self.__sides) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_lenght):
        super().__init__(color, *[side_lenght] * 12)
        self.__sides = side_lenght

    def get_volume(self):
        return self.__sides ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 9)
triangle1 = Triangle((100, 40, 254), 3, 4, 5)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
triangle1.set_color(2, 2, 2)
print(triangle1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

print(triangle1.get_square())