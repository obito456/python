import numpy as np

items=np.array([1,2,3])
cost=np.array([10,20,30])
bill1=np.dot(items,cost)
bill2=items @ cost
print(bill1,bill2)
