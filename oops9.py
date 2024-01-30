class Item:
    
    def __init__(self, name : str, quantity : float , price : float):
    
        self.name = name
        self.quantity = quantity
        self.price = price
        
        assert price >= o
        assert quantity >= o
                  
    def cal(self):
        return self.price * self.quantity

item1 = Item("chicken", -1 , 200 )
item2 = Item("onion", 2 , 30 )

print(item1.name)
print(item2.name)
print(item1.quantity)
print(item2.quantity)
print(item1.price)
print(item2.price)

print(item1.cal())
print(item2.cal())
