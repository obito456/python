class Item:
    def cal(self, a, b):
        return a * b
     

item1 = Item()
item1.name = "chicken"
item1.quantity = 1
item1.price = 200
print(item1.cal(item1.quantity,item1.price))

item2 = Item()
item2.name = "onion"
item2.quantity = 2
item2.price = 30
print(item2.cal(item2.quantity,item2.price))
