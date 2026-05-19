
class Product:

    def __init__(self, name, price, quantity):
        if name == "":
            raise ValueError("Name cannot be empty")
        self.name = name

        if price <= 0:
            raise ValueError("Price must be greater than 0")
        self.price = price

        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        self.quantity = quantity

        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            if self.quantity == 0:
                self.active = False
            return quantity * self.price
        return False


def main():
    try:
        bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
        mac = Product("MacBook Air M2", price=1450, quantity=100)

        print(bose.buy(50))
        print(mac.buy(100))
        print(mac.is_active())

        bose.show()
        mac.show()

        bose.set_quantity(1000)
        bose.show()

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()

