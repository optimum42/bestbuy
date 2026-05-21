import products
import store
import cart


def show_error(message):
    """
    prints an error message after an exception catching
    """
    print(f"######>{message}")


def print_menu(menu):
    """
    prints the CLI
    :param menu: menu as a dictionary
    """
    print("\n  Store Menu:")
    print("  -----------")
    for key, value in menu.items():
        print(f"{key}: {value[0]}")


def list_products(best_buy):
    """
    shows all available products
    :param best_buy: Store object
    """
    print("\n------")
    enumerated_products = enumerate(best_buy.get_all_products(), start=1)
    for number, product in enumerated_products:
        print(f"{number}: ", end="")
        product.show()
    print("------")


def get_order_quantity():
    """
    prompts the user to enter the quantity of the product
    :return: integer quantity
    """
    while True:
        quantity = input("How many do you want? ")
        try:
            quantity = int(quantity)
            if quantity == 0:
                raise ValueError
            return quantity
        except ValueError:
            print("Invalid input. Try again.")


def get_order(best_buy):
    """
    prompts the user to select a product from the previously listed products
    :param best_buy: Store object
    :return: product of Class Product or None if the user entered empty text
    """
    all_products = best_buy.get_all_products()
    while True:
        choice = input("\nWhich product # do you want (<Enter> to view cart)? ")
        try:
            if choice == "":
                return None, 0
            product_number = int(choice)
            if product_number < 1 or product_number > len(all_products):
                raise ValueError("Invalid input. Try again.")
            product = all_products[product_number - 1]
            quantity = get_order_quantity()
            return product, quantity

        except ValueError as e:
            show_error(e)


def order(best_buy):
    """
    Loop that allows the user to add products to the shopping cart.
    If the product is None, it shows the cart
    The user can then proceed to the checkout or continue adding products to the cart
    :param best_buy: Store object
    """
    shopping_cart = cart.Cart()
    while True:
        list_products(best_buy)
        product, quantity = get_order(best_buy)
        if product is not None:
            try:
                shopping_cart.add_product(product, quantity)
            except ValueError as e:
                show_error(e)

        else: # empty user choice, go to cart
            shopping_cart.show()
            if shopping_cart.is_empty():
                break

            print(f"--- Total price: ${shopping_cart.get_total_price():,.2f}")
            if input("\nProceed to checkout (y/n)? ") != 'y':
                continue

            # checkout
            try:
                total_price = best_buy.order(shopping_cart)
                print("********")
                print(f"Order made! Total payment: ${total_price:,.2f}")
            except ValueError as e:
                show_error(e)
            break


def show_total_store_amount(best_buy):
    """
    Shows the total number of all products
    :param best_buy: Store object
    """
    print(f"\nTotal quantity in store: {best_buy.get_total_quantity():,.0f} articles")


def quit_program(best_buy):
    """
    Quits the program on user request
    """
    print(f"\nQuitting {best_buy.name} store. Goodbye...!")
    quit()


def start(best_buy):
    """
    Mainloop that allows the user to choose from the menu
    If the store is empty, it shows a message and quits the program
    :param best_buy: Store object
    """
    menu = {
        1: ("List all products in store", list_products),
        2: ("Show total amount in store", show_total_store_amount),
        3: ("Make an order", order),
        4: ("Quit", quit_program),
    }
    while True:
        if len(best_buy.get_all_products()) == 0:
            print("No products available. Store closed!")
            break

        print_menu(menu)
        try:
            choice = int(input("Enter your choice: "))
            if choice not in menu:
                raise ValueError
            menu[choice][1](best_buy)
        except ValueError:
            print("Invalid input. Try again.")


def main():
    # initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]

    # create the store object
    best_buy = store.Store("Best Buy", product_list)

    # print a welcome message
    print(f"\n        Welcome to {best_buy.name} store!")
    print("        ==========================")
    print("""
        This is a simple CLI store application.
        
        You can list products, show the total amount in store, or make an order.
        To make an order, enter '3'.
            To add a product to the cart, enter the product number followed by the quantity.
            To remove a product from the cart, enter the product number followed by a negative quantity.
            You can also view the cart by entering an empty line.
            To proceed to checkout, enter 'y' and press Enter.
        To quit the program, enter '4'.
    """)

    # run the main loop
    start(best_buy)
    print("Goodbye!")


if  __name__ == "__main__":
    main()