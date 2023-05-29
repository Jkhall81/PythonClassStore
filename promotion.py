from abc import ABC, abstractmethod


class Promotion(ABC):
	name = ''

	@abstractmethod
	def apply_promotion(self, product, quantity):
		pass


class SecondHalfPrice(Promotion):
	name = 'Second Half Price!'

	def apply_promotion(self, product, quantity):
		if quantity % 2 == 0:
			half_quantity = quantity / 2
			total_price = (half_quantity * product.price) + (half_quantity * (product.price / 2))
			return float(total_price)
		else:
			half_quantity = (quantity - 1) / 2
			total_price = (half_quantity * product.price) + (half_quantity * (product.price / 2)) + product.price
			return float(total_price)


class ThirdOneFree(Promotion):
	name = 'Third One Free!'

	# this is all fucked up / review logic above also
	def apply_promotion(self, product, quantity):
		if quantity % 3 == 0:
			free_quantity = quantity / 3
			total_price = (quantity - free_quantity) * product.price
			return float(total_price)
		if quantity % 3 != 0:
			remainder = quantity % 3
			free_quantity = (quantity - remainder) / 3
			total_price = ((quantity - free_quantity) * product.price) + (remainder * product.price)
			return float(total_price)


class PercentDiscount(Promotion):
	name = 'Percent Discount!'

	def __init__(self, discount_percentage):
		self.discount_percentage = discount_percentage

	def apply_promotion(self, product, quantity):
		discounted_price = product.price * (1 - self.discount_percentage / 100)
		total_price = float(discounted_price * quantity)
		return round(total_price, 2)
