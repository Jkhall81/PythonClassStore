import pytest
from products import Product
from products import NonStockedProduct


# Unit Tests for the Product class!
# pass in (name, price, quantity)
def test_create_product():
	p = Product('fucking_fuck_fucks', 1450, 100)
	assert p.name == 'fucking_fuck_fucks'
	assert p.price == 1450
	assert p.quantity == 100
	assert p.is_active()


def test_create_invalid_product():
	with pytest.raises(ValueError) as error:
		Product('', -100, 0)
	assert str(error.value) == 'Product name cannot be empty!'


def test_quantity_zero_activate_product():
	with pytest.raises(ValueError) as error:
		Product('deez_nutz', 10, 0)
	assert str(error.value) == 'Quantity must be greater than zero!'


def test_product_purchase():
	p = Product('a$$_sandwich', 10, 20)
	total_price = p.buy(5)
	assert total_price == 50
	assert p.quantity == 15


def test_insufficient_quantity():
	p = Product('@n@l beads', 10, 20)
	with pytest.raises(ValueError) as error:
		p.buy(25)
	assert str(error.value) == 'Insufficient quantity available!'


def test_set_quantity_zero_deactivates_product():
	p = Product('fifth_of_scotch', 10, 5)
	assert p.is_active()
	try:
		p.set_quantity(0)
	except ValueError:
		pass
	assert not p.is_active()


# Unit Tests for the NonStockedProduct class!
# pass in (name, price)
def test_quantity_is_zero():
	p = NonStockedProduct('SomeShitName', 20)
	assert p.quantity == 0


pytest.main()
