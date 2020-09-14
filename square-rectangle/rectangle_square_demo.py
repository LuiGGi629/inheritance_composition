class Rectangle:
    def __init__(self, length, height) -> None:
        self._length = length
        self._height = height

    @property
    def area(self):
        return self._length * self._height


class Square(Rectangle):
    def __init__(self, side_size) -> None:
        super().__init__(side_size, side_size)


rectangle = Rectangle(2, 4)
assert rectangle.area == 8

square = Square(2)
assert square.area == 4

print("OK!")
