class Item:
	
    def __init__(self, name, price):
    	print("It is %s and its cost is %d." %(name, price))
    	#print(f"it is {name}")
        #print("It is {}".format(name))

    def cal(self, a, b):
        return a * b
     

item1 = Item("chicken", 200)
item1.name = "chicken"
item1.quantity = 1
item1.price = 200


item2 = Item("onion", 30)
item2.name = "onion"
item2.quantity = 2
item2.price = 30
