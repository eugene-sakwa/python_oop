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
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    #Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    #Property Decorator = Set attribute for read only 
    def name(self, new_name):
        if len(new_name) > 10:
            raise Exception( 'The name is too long!')
        else:
            self.__name = new_name
    

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

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
    
