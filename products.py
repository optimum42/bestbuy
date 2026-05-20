
class Product:
    """
    The product class that holds the product name, price, and quantity
    and allows the user to operate on the product
    """
    def __init__(self, name, price, quantity):
        if name == "":
            raise ValueError(f"{name}: Name cannot be empty")
        self.name = name

        if price <= 0:
            raise ValueError(f"{name}: Price must be greater than 0")
        self.price = price

        if quantity <= 0:
            raise ValueError(f"{name}: Quantity must be greater than 0")
        self.quantity = quantity

        self.active = True

    def get_quantity(self):
        return self.quantity

    def get_price(self):
        return self.price

    def set_quantity(self, quantity):
        if quantity <= 0:
            raise ValueError(f"{self.name}: Quantity must be greater than 0")
        self.quantity = quantity

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: ${self.price:,.2f}, Quantity: {self.quantity:,.0f}")

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError(f"{self.name}: Quantity must be greater than 0")
        if quantity > self.quantity:
            raise ValueError(f"{self.name}: {quantity} exceeds the maximum quantity of {self.quantity}")

        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False
        return quantity * self.price


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

