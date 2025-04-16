import csv

class Item:

    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        # Run validation to the received arguments
        assert price >= 0, f'Price {price} is not greater than or equal to 0'
        assert quantity >= 0, f' Quantity {quantity} is not greater than or equal to 0'
        
        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    #Property Decorator = Read-Only Attribute
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increament(self, increament_value):
        self.__price = self.__price + self.price * increament_value

    
    #Property Decorator = Set attribute for read only 
    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            raise Exception( 'The name is too long!')
        else:
            self.__name = new_name

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise Exception( 'The price cannot be below 0')
        else:
            self.__price = new_price
    

    def calculate_total_price(self):
        return self.__price * self.quantity
    

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r' ) as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))

            )
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer
        
        elif isinstance(num, int):
            return True
        
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity}')"
    
