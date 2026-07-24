from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract base class for all promotions."""

    def __init__(self, name):
        """Creates a promotion."""
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Returns the price after applying the promotion."""
        pass


class SecondHalfPrice(Promotion):
    """Applies a half-price promotion to every second item."""

    def apply_promotion(self, product, quantity):
        """Returns the price after applying the promotion."""
        full_items = quantity - (quantity // 2)
        half_items = quantity // 2

        return (
            full_items * product.price
            + half_items * product.price * 0.5
        )


class ThirdOneFree(Promotion):
    """Makes every third item free."""

    def apply_promotion(self, product, quantity):
        """Returns the price after applying the promotion."""
        return (quantity - (quantity // 3)) * product.price


class PercentDiscount(Promotion):
    """Applies a percentage discount."""

    def __init__(self, name, percentage):
        """Creates a percentage discount promotion."""
        super().__init__(name)

        if not isinstance(percentage, (int, float)):
            raise ValueError("Percentage must be a number.")

        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100.")

        self.percentage = percentage

    def apply_promotion(self, product, quantity):
        """Returns the price after applying the promotion."""
        return (
            quantity
            * product.price
            * ((100 - self.percentage) / 100)
        )