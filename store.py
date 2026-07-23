class Store:
    """Represents a store containing products."""

    def __init__(self, product_list):
        """Creates a store with a product list."""
        self.product_list = product_list

    def add_product(self, product):
        """Adds a product to the store."""
        self.product_list.append(product)

    def remove_product(self, product):
        """Removes a product from the store."""
        self.product_list.remove(product)

    def get_total_quantity(self):
        """Returns the total quantity in the store."""
        total_quantity = 0

        for product in self.product_list:
            total_quantity += product.get_quantity()

        return total_quantity

    def get_all_products(self):
        """Returns all active products."""
        active_products = []

        for product in self.product_list:
            if product.is_active():
                active_products.append(product)

        return active_products

    def order(self, shopping_list):
        """Processes an order and returns its price."""
        total_price = 0

        for product, quantity in shopping_list:
            if product not in self.product_list:
                raise ValueError("Product is not available in this store.")

            total_price += product.buy(quantity)

        return total_price
