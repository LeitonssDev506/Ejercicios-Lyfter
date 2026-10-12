

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height


    def is_valid_number(self):
        if self.width < 0 or self.height < 0:
            raise ValueError("There is at least one negative value! Please enter a positive value")

    def get_area(self):

        self.is_valid_number()
        self.area = (self.width * self.height)
        return self.area

    def get_perimeter(self):

        self.is_valid_number()
        self.perimeter = 2*(self.width + self.height)

        return self.perimeter

try:
    height = int(input("Type the height: "))
    width = int(input("Type the width: "))

    rectangle = Rectangle(width, height)

    print(rectangle.get_area())
    print(rectangle.get_perimeter())

except ValueError as error:
    print(f"Error: {error}")
