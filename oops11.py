class Item:
	
    payrate= 0.9
    
    def __init__(self, name: str, quantity: int, price: float):
        assert price >= 0
        assert quantity >= 0
    
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def cal(self):
        return self.price * self.quantity
    
    def discount(self):
    	self.price = self.price * self.payrate

item1 = Item("chicken", 1, 200)
item2 = Item("onion", 2, 30)

item2.payrate = 0.5

item1.discount()
item2.discount()

print(item1.price)
print(item2.price)

