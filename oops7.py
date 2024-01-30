class Item:
    
    def __init__(self, name, quantity, price=100):
        self.name = name
        self.quantity = quantity
        self.price = price

item1 = Item("chicken", 1)
item2 = Item("onion", 2)

print(item1.name)
print(item2.name)
print(item1.quantity)
print(item2.quantity)
print(item1.price)
print(item2.price)
