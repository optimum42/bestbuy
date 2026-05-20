import products


class Store:
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total_quantity(self):
        total = 0
        for product in self.product_list:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        return [product for product in self.product_list if product.is_active()]

    def order(self, shopping_list):
        total_amount = 0
        for position in shopping_list:
            product, quantity = position
            if product not in self.get_all_products():
                raise ValueError(f"{product.name}: Product not available")
            if quantity <= 0:
                raise ValueError(f"{product.name}: Quantity must be greater than 0")
            if quantity > product.get_quantity():
                raise ValueError(f"{product.name}: {quantity} exceeds the maximum quantity of {product.get_quantity()}")
            total_amount += product.buy(quantity)
        return total_amount


def main():

    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    all_products = best_buy.get_all_products()

    print("Available products\n--------------------------")
    for product in all_products:
        product.show()
    print(f"Total quantity: {best_buy.get_total_quantity()}")

    print("\nBuying products\n--------------------------")
    dummy_product = products.Product("Dummy Product", price=100, quantity=100)
    order_list = [(all_products[0], 1), (all_products[1], 2), (dummy_product, 5)]
    for product, quantity in order_list:
        print(f"Buying {quantity} {product.name}: {product.price * quantity}")
    try:
        total_amount = best_buy.order(order_list)
        print(f"Total amount: {total_amount}")
    except ValueError as e:
        print(e)

    print("\nAvailable products\n--------------------------")
    for product in all_products:
        product.show()
    print(f"Total quantity: {best_buy.get_total_quantity()}")


if __name__ == "__main__":
    main()