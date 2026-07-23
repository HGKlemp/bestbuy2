class Product:
    """Represents a product in the store."""

    def __init__(self, name, price, quantity, active=True):
        """Creates a new product."""
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")

        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")

        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        if not isinstance(active, bool):
            raise ValueError("Active must be a boolean.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active

    def get_quantity(self):
        """Returns the available quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """Updates the available quantity."""
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Returns whether the product is active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Returns the product information."""
        return (
            f"{self.name}, Price: {self.price}, "
            f"Quantity: {self.quantity}"
        )

    def buy(self, quantity):
        """Buys a quantity and returns its price."""
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Purchase quantity must be a positive integer.")

        if quantity > self.quantity:
            raise ValueError(
                "Purchase quantity is greater than the available quantity."
            )

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return quantity * self.price


class NonStockedProduct(Product):
    """Represents a product whose quantity is not tracked."""

    def __init__(self, name, price):
        """Creates a non-stocked product."""
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        """Keeps the quantity permanently at zero."""
        self.quantity = 0

    def show(self):
        """Returns the non-stocked product information."""
        product_information = super().show()

        return product_information.replace(
            "Quantity: 0",
            "Quantity: Unlimited"
        )

    def buy(self, quantity):
        """Returns the price without changing the quantity."""
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Purchase quantity must be a positive integer.")

        return quantity * self.price


class LimitedProduct(Product):
    """Represents a product with a purchase limit."""

    def __init__(self, name, price, quantity, maximum):
        """Creates a limited product."""
        super().__init__(name, price, quantity)

        if not isinstance(maximum, int) or maximum <= 0:
            raise ValueError("Maximum must be a positive integer.")

        self.maximum = maximum

    def show(self):
        """Returns the limited product information."""
        product_information = super().show()

        return (
            f"{product_information}, "
            f"Limited to {self.maximum} per order"
        )

    def buy(self, quantity):
        """Buys a quantity if it does not exceed the limit."""
        if quantity > self.maximum:
            raise ValueError(
                f"Only {self.maximum} items can be purchased per order."
            )

        return super().buy(quantity)