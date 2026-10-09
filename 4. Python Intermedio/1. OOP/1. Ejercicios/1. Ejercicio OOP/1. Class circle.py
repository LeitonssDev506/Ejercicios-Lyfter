

class circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        Area = 3.14159*((self.radius)**2)
        print(f"The area of the circle is: {Area}")


result = circle(20)
result.get_area()

