import pytest
from products import Product
from products import NonStockedProduct
from products import LimitedProduct
from promotion import PercentDiscount
from promotion import ThirdOneFree


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


# Unit Tests for the LimitedProduct class!
# pass in (name, price, quantity, maximum)
def test_maximum_is_correct():
	p = LimitedProduct('name', 10, 10, 1)
	assert p.maximum == 1
	p1 = LimitedProduct('name', 10, 10, 2)
	assert p1.maximum == 2


# Testing updated show method!
def test_show_method_with_promotion():
	p = Product('Example Product', 10, 20)
	promotion = PercentDiscount(10)
	p.promotion = promotion
	expected_output = 'Example Product, Price: 10, Quantity: 20, Promotion: Percent Discount!'
	assert p.show() == expected_output
	p1 = Product('name', 10, 20)
	promotion = ThirdOneFree()
	p1.promotion = promotion
	expected_output2 = 'name, Price: 10, Quantity: 20, Promotion: Third One Free!'
	assert p1.show() == expected_output2


# Testing updated buy method!  Should be using apply_promotion if promotion is set!  let's get nashty....
def test_buy_with_promotion():
	product = Product('Product', 10, 20)
	promotion = PercentDiscount(10)
	product.promotion = promotion
	total_price = product.buy(10)
	# some quick maths.... 10% off 10 is 9 for qty 10 is 90
	assert total_price == 90
	# fucking shit works....  Muahaahaaahaaaahaaa


def test_buy_without_promotion():
	product = Product('Product', 10, 20)
	total_price = product.buy(10)
	# we're looking at an even hundo
	assert total_price == 100
	# Boomshakalaka


pytest.main()
