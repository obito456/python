class Item:
	
    payrate= 0.5
    
    def __init__(self, name: str, quantity: int, price: float):
        assert price >= 0
        assert quantity >= 0
    
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def cal(self):
        return self.price * self.quantity
    

item1 = Item("chicken", 1, -200)
item2 = Item("onion", 2, -30)

print(Item.__dict__)
print(item1.__dict__)
print(item2.__dict__)
