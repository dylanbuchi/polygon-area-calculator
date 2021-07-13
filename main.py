import shape_calculator
from unittest import main

rectangle = shape_calculator.Rectangle(5, 10)
print(rectangle.get_area())
rectangle.set_width(3)
print(rectangle.get_perimeter())
print(rectangle)

square = shape_calculator.Square(9)
print(square.get_area())
square.set_side(4)
print(square.get_diagonal())
print(square)

# Run unit tests automatically
main(module='test', exit=False)