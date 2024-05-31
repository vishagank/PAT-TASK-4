class Square:
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * 2

    def calculate_perimeter(self):
        return 4 * self.side

# Given list
sides = [10, 501, 22, 37, 100, 999, 87, 351]


areas = []
perimeters = []

for sides in sides:
     square = Square(sides)
     areas.append(square.calculate_area())
     perimeters.append(square.calculate_perimeter())


print("Areas:", areas)
print("Perimeters:", perimeters)
