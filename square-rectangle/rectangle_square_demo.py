class Rectangle:
    def __init__(self, length, height) -> None:
        self._length = length
        self._height = height

    @property
    def area(self):
        return self._length * self._height

    def resize(self, new_length, new_height):
        self._length = new_length
        self._height = new_height


class Square(Rectangle):
    def __init__(self, side_size) -> None:
        super().__init__(side_size, side_size)


rectangle = Rectangle(2, 4)
assert rectangle.area == 8

rectangle.resize(3, 5)
assert rectangle.area == 15

square = Square(2)
assert square.area == 4

square.resize(3, 5)
print(f"Square area: {square.area}")

# print("OK!")
