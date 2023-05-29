import products
import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def start(best_buy):
	"""This function displays a menu to the user and basically gives the user
	access to the product and store class."""

	func_dict = {
		1: get_all_products,
		2: show_total_amount_of_inventory,
		3: make_an_order
	}
	menu_str = """
	
		1. List all products in store
		2. Show total amount in store
		3. Make an order
		4. Quit
		
	"""

	while True:
		print(menu_str)
		user_input = input('Please choose an option: ')

		if int(user_input) == 4:
			break

		func_dict[int(user_input)]()


def get_all_products():
	"""This function basically just calls the show method for each item in the
	best_buy list."""
	active_products = best_buy.get_all_products()
	for item in active_products:
		print(item.show())


def make_an_order():
	"""This function prompts the user for a product name and quantity, and will then
	use the buy method to make a purchase.  The function will return the item purchased,
	the quantity purchased, and the total price to the user."""

	customer_order = []
	total_price = 0

	while True:
		product_name = input('Please enter the product name: ')
		product_quantity = int(input('Enter the product quantity: '))

		product = None
		for prod in best_buy.product_list:
			if prod.name == product_name:
				product = prod
				break

		if product is None:
			print('Product not found!')
			continue

		if product_quantity > product.quantity:
			print('Insufficient quantity in stock!')
			continue

		price = product.buy(product_quantity)
		total_price += price
		customer_order.append((product, product_quantity))

		another_purchase = input('Do you want to make another purchase? (y/n): ')
		if another_purchase.lower() != 'y':
			break

	print('Thank you for shopping with us!')
	print('Your order:')
	for item in customer_order:
		print(f'Product: {item[0].name}, Quantity: {item[1]}')
	print(f'Total Price: {total_price}')


def show_total_amount_of_inventory():
	print(best_buy.get_total_quantity())


def main():
	start(best_buy)


if __name__ == '__main__':
	main()
