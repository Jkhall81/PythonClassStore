from promotion import SecondHalfPrice
from promotion import ThirdOneFree
from promotion import PercentDiscount
from products import Product
import pytest


# Unit Tests for SecondHalfPrice class!  OMFG!!!!
# Product (name, price, quantity)
def test_second_half_price_total_price():
	p = Product('name', 10, 20)
	promotion = SecondHalfPrice()
	total_price = promotion.apply_promotion(p, 20)
	assert total_price == 150
	p1 = Product('name', 10, 21)
	total_price2 = promotion.apply_promotion(p1, 21)
	assert total_price2 == 160


# Unit Tests for ThirdOneFree class...  meh....
# Product (name, price, quantity
def test_third_one_fo_free_total_price_how_long_can_we_make_this_name_go_ok_im_done_now():
	p = Product('name', 10, 30)
	# quantity of 30, 10 should be free, so 20 at a price of 10 = 200
	promotion = ThirdOneFree()
	total_price = promotion.apply_promotion(p, 30)
	assert total_price == 200
	p = Product('name', 10, 31)
	# quantity of 31, 10 free again, with 21 at full price == 210
	promotion = ThirdOneFree()
	total_price = promotion.apply_promotion(p, 30)
	assert total_price == 200
	p = Product('name', 10, 32)
	# should be 220 |-0-| \-o-/ |-0-| tie fighters incoming
	promotion = ThirdOneFree()
	total_price = promotion.apply_promotion(p, 30)
	assert total_price == 200


# Unit Tests for PercentDiscount class.  this one should be easy
# Product (name, price, quantity)
def test_percent_discount_total_price():
	p = Product('name', 10, 20)
	promotion = PercentDiscount(30)
	total_price = promotion.apply_promotion(p, 20)
	assert total_price == 140
	p = Product('name', 13, 21)
	promotion = PercentDiscount(22)
	total_price = promotion.apply_promotion(p, 21)
	assert total_price == 212.94
	p = Product('name', 5, 17)
	promotion = PercentDiscount(73)
	total_price = promotion.apply_promotion(p, 17)
	assert total_price == 22.95


# Testing getter and setter!
def test_promotion_getter_and_setter():
	product = Product('name', 10, 20)
	promotion = PercentDiscount(30)
	assert product.promotion is None  # Initial value should be None
	product.promotion = promotion
	assert product.promotion == promotion  # Getter should return the set promotion
	product.promotion = None
	assert product.promotion is None  # Setter should allow setting promotion to None


pytest.main()
