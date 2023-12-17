class Coffee:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, "name"):
            if isinstance(name, str):
                self._name = name
            else:
                raise TypeError("Name must be a string")
        
    def orders(self):
        coffee_orders = [order for order in Order.all if order.coffee == self]
        return coffee_orders
    
    def customers(self):
        coffee_customers = [order.customer for order in Order.all if order.coffee == self]
        unique_list = []
        for customer in coffee_customers:
            if customer not in unique_list:
                unique_list.append(customer)
        return unique_list
    
    def num_orders(self):
        coffee_orders = [order for order in Order.all if order.coffee == self]
        return len(coffee_orders)
    
    def average_price(self):
        coffee_price_list = [order.price for order in Order.all if order.coffee == self]
        average_price = sum(coffee_price_list) / len(coffee_price_list)
        return average_price

class Customer:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            #raise TypeError("Name must be a string")
            print("Name must be a string")
        
    def orders(self):
        coffee_orders = [order for order in Order.all if order.customer == self]
        unique_list = []
        for order in coffee_orders:
            if order not in unique_list:
                unique_list.append(order)
        return unique_list
    
    def coffees(self):
        coffee_list = [order.coffee for order in Order.all if order.customer == self]
        unique_list = []
        for coffee in coffee_list:
            if coffee not in unique_list:
                unique_list.append(coffee)
        return unique_list
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order

#Order acts as the (one) where it keeps track of the customer, coffee, and its own order
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise TypeError("Customer must be a Customer object")
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise TypeError("Coffee must be a Coffee object")
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if not hasattr(self, 'price'):
            if isinstance(price, (int, float)):
                self._price = price
            else:
                #raise TypeError("Price must be an Integer")
                print("Price must be an Integer")

