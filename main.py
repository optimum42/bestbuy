import products
import store


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
    for no, product in enumerated_products:
        print(f"{no}: ", end="")
        product.show()
    print("------")


def get_order_product(best_buy):
    """
    prompts the user to select a product from the previously listed products
    :param best_buy: Store object
    :return: product of Class Product or None if the user entered empty text
    """
    all_products = best_buy.get_all_products()
    while True:
        no = input("\nWhich product # do you want (Enter empty text to view cart)? ")
        try:
            if no == "":
                return None
            product_list_index = int(no)
            if product_list_index < 1 or product_list_index > len(all_products):
                raise ValueError
            return all_products[product_list_index-1]
        except ValueError:
            print("Invalid input. Try again.")


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


def add_product_to_cart(product, shopping_list):
    """
    adds a product to the shopping list (cart) and adjusts the quantity if already in cart
    :param product: product to be added to the cart
    :param shopping_list: the shopping list (cart)
    :return: shopping list (cart) with the new or adjusted product
    """
    cart_quantity = 0
    item = None

    # check if the product is already in the cart
    for item in shopping_list:
        if item[0] == product:
            cart_quantity = item[1]

    quantity = get_order_quantity()
    if quantity < 0 and abs(quantity) > cart_quantity:
        print(f"{product.name}: Your cart only holds {cart_quantity:.0f} articles - you cannot order less.")
        return shopping_list
    elif quantity > product.get_quantity():
        print(f"Sorry, we only have {product.get_quantity():,.0f} in stock.")
        return shopping_list
    elif cart_quantity > 0: # already in cart - adjust quantity
        quantity += cart_quantity
        shopping_list.remove(item)
    if quantity != 0:
        shopping_list.append((product, quantity))
        print(f"{product.name}: {quantity:,.0f} are now in your cart!")
    else:
        print(f"{product.name}: Removed from cart")
    return shopping_list


def order(best_buy):
    """
    Loop that allows the user to add products to the shopping cart.
    If the product is None, it shows the cart
    The user can then proceed to the checkout or continue adding products to the cart
    :param best_buy: Store object
    """
    list_products(best_buy)
    shopping_list = []
    while True:
        product = get_order_product(best_buy)
        if product is not None:
            shopping_list = add_product_to_cart(product, shopping_list)
        else: # empty user choice, go to cart
            if len(shopping_list) == 0:
                print("\n*** Your cart is empty!")
                break

            # show cart
            print("\n*** Your cart")
            total_price = 0
            for product, quantity in shopping_list:
                total_price += product.get_price() * quantity
                print(f"{product.name}: {quantity:,.0f}")
            print(f"Total price: ${total_price:,.2f}")
            if input("\nProceed to checkout (y/n)? ") != 'y':
                continue

            # checkout
            try:
                total_price = best_buy.order(shopping_list)
                print("********")
                print(f"Order made! Total payment: ${total_price:,.2f}")
            except ValueError as e:
                print(e)
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
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=5000),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]

    # create the store object
    best_buy = store.Store("Best Buy", product_list)

    # run the main loop
    start(best_buy)
    print("Goodbye!")


if  __name__ == "__main__":
    main()