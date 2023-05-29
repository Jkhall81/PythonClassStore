class Product:
    def __init__(self, name, price, quantity):
        try:
            self.name = name
            if self.name == '':
                raise ValueError('Product name cannot be empty!')

            self.price = price
            if self.price < 0:
                raise ValueError('Price cannot be less than zero!')

            self.quantity = quantity
            if self.quantity <= 0:
                raise ValueError('Quantity must be greater than zero!')

            self.active = True

        except Exception as e:
            print(f'An error occurred: {str(e)}')
            raise e

    def get_quantity(self):
        output = float(self.quantity)
        return output

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        output = f'{self.name}, Price: {self.price}, Quantity: {self.quantity}'
        return output

    def buy(self, quantity):
        if quantity <= 0:
            raise Exception('Quantity must be greater than zero!')
        if quantity > self.quantity:
            raise ValueError('Insufficient quantity available!')
        self.quantity -= quantity
        total_price = self.price * quantity
        return float(total_price)


class NonStockedProduct(Product):
    def __init__(self, name, price):
        try:
            super().__init__(name, price, 0)
        except ValueError:
            self.quantity = 0

    def show(self):
        output = f'{self.name}, Price: {self.price}, Quantity: Unlimited'
        return output


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        output = f'{self.name}, Price: {self.price}, Quantity: {self.quantity} Maximum: {self.maximum}'
        return output
