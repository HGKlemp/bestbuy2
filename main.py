import products
from promotion import (
    PercentDiscount,
    SecondHalfPrice,
    ThirdOneFree,
)
from store import Store


def show_products(best_buy):
    """Display all active products."""
    product_list = best_buy.get_all_products()

    print("\n------ Product List ------")

    for index, product in enumerate(product_list, start=1):
        print(f"{index}. {product.show()}")


def show_total_quantity(best_buy):
    """Display the total product quantity."""
    total_quantity = best_buy.get_total_quantity()
    print(f"\nTotal amount in store: {total_quantity}")


def create_shopping_list(best_buy):
    """Create a shopping list from user input."""
    shopping_list = []
    product_list = best_buy.get_all_products()

    while True:
        show_products(best_buy)

        product_number = input(
            "\nEnter product number "
            "(or press ENTER to finish): "
        )

        if not product_number:
            break

        try:
            product_number = int(product_number)

            if not 1 <= product_number <= len(product_list):
                print("Invalid product number.")
                continue

            quantity = int(input("Enter quantity: "))

            shopping_list.append(
                (product_list[product_number - 1], quantity)
            )

            print("Product added to the shopping list.")

        except ValueError:
            print("Please enter valid numbers.")

    return shopping_list


def make_order(best_buy):
    """Create and process an order."""
    shopping_list = create_shopping_list(best_buy)

    if not shopping_list:
        print("No products selected.")
        return

    try:
        total_price = best_buy.order(shopping_list)
        print("\nOrder completed!")
        print(f"Total price: ${total_price}")

    except ValueError as error:
        print(error)


def start(best_buy):
    """Start the store menu."""
    while True:
        print("\n========== Best Buy ==========")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("\nPlease choose a number: ")

        if choice == "1":
            show_products(best_buy)

        elif choice == "2":
            show_total_quantity(best_buy)

        elif choice == "3":
            make_order(best_buy)

        elif choice == "4":
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Please choose a number from 1 to 4.")


def main():
    """Create the inventory and start the program."""
    second_half_price = SecondHalfPrice("Second Half Price")
    third_one_free = ThirdOneFree("Third One Free")
    thirty_percent = PercentDiscount("Thirty Percent", 30)

    macbook = products.Product(
        "MacBook Air M2",
        price=1450,
        quantity=100,
    )
    bose_quiet_comfort = products.Product(
        "Bose QuietComfort Earbuds",
        price=250,
        quantity=500,
    )
    google_pixel = products.Product(
        "Google Pixel 7",
        price=500,
        quantity=250,
    )
    windows_license = products.NonStockedProduct(
        "Windows License",
        price=125,
    )
    shipping = products.LimitedProduct(
        "Shipping",
        price=10,
        quantity=250,
        maximum=1,
    )

    macbook.set_promotion(thirty_percent)
    bose_quiet_comfort.set_promotion(second_half_price)
    google_pixel.set_promotion(third_one_free)

    product_list = [
        macbook,
        bose_quiet_comfort,
        google_pixel,
        windows_license,
        shipping,
    ]

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()