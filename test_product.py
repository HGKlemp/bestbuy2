import pytest
from products import Product


def test_create_product_ok():
    macbook = Product("MacBook Air M2", 1450, 100)

    assert macbook.name == "MacBook Air M2"
    assert macbook.price == 1450
    assert macbook.quantity == 100
    assert macbook.is_active() is True


def test_create_product_empty_name():
    with pytest.raises(ValueError):
        Product("", 1450, 100)


def test_create_product_negative_price():
    with pytest.raises(ValueError):
        Product("MacBook Air M2", -10, 100)


def test_product_becomes_inactive():
    product = Product("MacBook Air M2", 1450, 5)

    product.buy(5)

    assert product.quantity == 0
    assert product.is_active() is False

def test_product_amount_changes_quantity():
    product = Product("MacBook Air M2", 1450, 5)

    product.buy(2)

    assert product.quantity == 3


def test_product_buy_too_much():
    product = Product("MacBook Air M2", 1450, 5)

    with pytest.raises(ValueError):
        product.buy(10)