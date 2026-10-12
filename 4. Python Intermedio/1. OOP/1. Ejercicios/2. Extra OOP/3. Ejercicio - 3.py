
class Product:

    def __init__(self, name , price, amount):

        self.name = name
        self.price = price
        self.amount = amount
    

class Inventory:

    def __init__(self):
        self.products = []


    def add_products(self, product):

        self.products.append(product)


    def display_products(self):

        for product in self.products:
            print(product.name)

    def calculate_total_value_of_inventory(self):

        total_value = 0
        for product in self.products:
            total = product.price * product.amount
            total_value += total
        
        return total_value
        


product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)

inventory = Inventory()

inventory.add_products(product1)

inventory.add_products(product2)

inventory.display_products()

value_of_inventory = inventory.calculate_total_value_of_inventory()
print(value_of_inventory)



