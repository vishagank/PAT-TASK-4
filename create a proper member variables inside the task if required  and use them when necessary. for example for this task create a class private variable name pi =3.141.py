
class circle:
 __pi = 3.141

 def __init__(self,radius):
    self.radius = radius

 def area(self):
    return circle.__pi * self.radius ** 2

 def circumference(self):
    return 2 * circle.__pi * self.radius


circle = circle(2)
print(f"area: {circle.area()}")
print(f"circumference: {circle.circumference()}")