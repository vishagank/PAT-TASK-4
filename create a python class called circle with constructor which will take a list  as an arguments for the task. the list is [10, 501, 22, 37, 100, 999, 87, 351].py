class Circle:

    def __init__(self, radius_list):

        self.radius_list = radius_list


radii = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii)


print(circle.radius_list)
