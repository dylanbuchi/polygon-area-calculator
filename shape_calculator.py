from __future__ import annotations


class Rectangle:

    MAX_WIDTH_AND_HEIGHT = 50
    IS_TOO_BIG_STRING = "Too big for picture."

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def set_width(self, new_width: int) -> None:
        self.width = new_width

    def set_height(self, new_height: int) -> None:
        self.height = new_height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> float:
        return (self.width**2 + self.height**2)**0.5

    def get_picture(self) -> str:
        if self._is_too_big():
            return self.IS_TOO_BIG_STRING
        return self._create_picture()

    def get_amount_inside(self, shape: Rectangle):
        return self.get_area() // shape.get_area()

    def _is_too_big(self) -> bool:
        return self.width > self.MAX_WIDTH_AND_HEIGHT or self.height > self.MAX_WIDTH_AND_HEIGHT

    def _get_class_name(self) -> str:
        return type(self).__name__.capitalize()

    def _create_picture(self) -> str:
        picture = []
        for _ in range(self.height):
            for _ in range(self.width):
                picture.append("*")
            picture.append("\n")
        return ''.join(picture)

    def __repr__(self) -> str:
        return f"{self._get_class_name()}(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side: int) -> None:
        super().__init__(side, side)

    def set_side(self, side: int) -> None:
        super().set_height(side)
        super().set_width(side)

    def __repr__(self) -> str:
        return super()._get_class_name() + f"(side={self.width})"
