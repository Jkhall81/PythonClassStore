import pytest
from store import Store
from products import Product


def test_add_product():
	store = Store([])
	product = Product('Test Product', 10, 20)
	store.add_product(product)
	assert len(store.product_list) == 1
	assert store.product_list[0] == product


def test_remove_product():
	product1 = Product('Product 1', 10, 20)
	product2 = Product('Product2', 15, 30)
	store = Store([product1, product2])
	assert len(store.product_list) == 2
	store.remove_product(product1)
	assert len(store.product_list) == 1
	assert store.product_list[0] == product2


def test_get_total_quantity():
	product1 = Product('Product1', 10, 20)
	product2 = Product('Product2', 15, 30)
	store = Store([product1, product2])
	assert store.get_total_quantity() == 50


def test_get_all_products():
	product1 = Product('Product 1', 10, 20)
	product2 = Product('Product 2', 15, 30)
	store = Store([product1, product2])
	products = store.get_all_products()
	assert len(products) == 2
	assert product1 in products
	assert product2 in products


def test_order():
	product1 = Product('Product 1', 10, 20)
	product2 = Product('Product 2', 15, 30)
	store = Store([product1, product2])
	shopping_list = [(product1, 5), (product2, 3)]
	total_price = store.order(shopping_list)
	assert total_price == 95.0


def test_order_with_insufficient_quantity():
	product1 = Product('Product 1', 10, 20)
	product2 = Product('Product 2', 15, 30)
	store = Store([product1, product2])
	shopping_list = [(product1, 25), (product2, 40)]
	total_price = store.order(shopping_list)
	assert total_price == 0


pytest.main()
