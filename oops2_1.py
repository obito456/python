class Item:
    def cal(a,b):              #use self parameter
        return a,b

item1 = Item()
item1.name = "chicken"
item1.quantity = 1
item1.price = 200
print(item1.cal(item1.name))

#print(item1.cal("name"))
