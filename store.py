class Store:
	def __init__(self, product_list):
		self.product_list = product_list

	def add_product(self, product):
		self.product_list.append(product)

	def remove_product(self, product):
		self.product_list.remove(product)

	def get_total_quantity(self):
		product_quantity_sum = 0
		for item in self.product_list:
			if item.active:
				product_quantity_sum += item.quantity
		return int(product_quantity_sum)

	def get_all_products(self):
		active_products = [product for product in self.product_list if product.active is True]
		return list(active_products)

	def order(self, shopping_list):
		total_price = 0
		for item in shopping_list:
			prod_obj = item[0]
			prod_quantity = item[1]
			try:
				price = prod_obj.buy(prod_quantity)
				total_price += float(price)
			except ValueError as e:
				print(f'Error ordering product "{prod_obj.name}": {str(e)}')
		return float(total_price)
