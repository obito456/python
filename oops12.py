class Item:
	
    payrate= 0.9
    
    a=[] 
    
    def __init__(self, name: str, quantity: int, price: float):
    
        assert price >= 0
        assert quantity >= 0
    
        self.name = name
        self.quantity = quantity
        self.price = price
        
        Item.a.append(self)
        
    def cal(self):
        return self.price * self.quantity
    
    def discount(self):
    	self.price = self.price * self.payrate

item1 = Item("chicken", 1, 200)
item2 = Item("onion", 2, 30)
item3 = Item("Mutton", 1, 800)
item4 = Item("oil", 2, 300)

print(Item.a)

for i in Item.a:
	print(i.name)
