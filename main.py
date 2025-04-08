class Item:
    def __init__(self, name: str, price: float, quantity = 0):
        # Run validation to the received arguments
        assert price >= 0, f'Price {price} is not greater than or equal to 0'
        assert quantity >= 0, f' Quantity {quantity} is not greate than or equal to 0'
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity



item1 = Item('Phone', 100, 5)
item1.name = 'Phone'
item1.price = 100
item1.quantity = 5


item2 = Item('Laptop', 1000, 3)
item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 3
