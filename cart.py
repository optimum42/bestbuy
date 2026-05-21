import products

class Cart:
    """
    The Cart class that holds all products in the shopping cart
    and manages the addition, removal, and total price of the products
    """
    def __init__(self, new_products=None):
        new_products = new_products or {}
        self.products = new_products

    def is_empty(self):
        return not self.products

    def add_product(self, product, quantity=1):
        # check if the product is available
        if not product.is_active():
            raise ValueError(f"{product.name}: Product not available")

        if product in self.products:
            quantity += self.products[product]

        # check if the quantity is greater than 0
        if quantity < 0:
            raise ValueError(f"{product.name}: Total cart quantity must be greater than 0")

        # check if the quantity in stock is enough
        if quantity > product.get_quantity():
            raise ValueError(f"{product.name}: {quantity} exceeds the maximum quantity of {product.get_quantity()}")

        # remove product if quantity is 0
        if quantity == 0 and product in self.products:
            del self.products[product]

        # add product to cart or update quantity
        if quantity > 0:
            self.products[product] = quantity

    def show(self):
        if not self.products:
            print("*** Your cart is empty!")
            return

        print("\n*** Your cart:")
        for product, quantity in self.products.items():
            print(f"{product.name}: ${product.price:,.2f}, Quantity: {quantity:,.0f}")

    def get_total_price(self):
        total_price = 0
        for product, quantity in self.products.items():
            total_price += product.get_price() * quantity
        return total_price


def main():
    mac_book = products.Product("MacBook Air M2", price=1450, quantity=100)
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    pixel7 = products.Product("Google Pixel 7", price=500, quantity=250)

    initial_cart = {mac_book: 2, bose: 1, pixel7: 1}
    cart = Cart(initial_cart)

    show_total = lambda x=None: print(f"===Total price: ${cart.get_total_price():,.2f}")

    cart.show()
    show_total()

    try:
        cart.add_product(mac_book, -2)
        cart.add_product(bose, -1)
        cart.add_product(pixel7, -1)
    except ValueError as e:
        print(f"######>{e}")
    finally:
        cart.show()
        show_total()


if __name__ == "__main__":
    main()