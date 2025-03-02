import numpy as np

items=np.array([[1,2,3],[4,5,6]])
cost=np.array([7,8,9])
bill1=np.dot(items,cost)
bill2=items @ cost
print(bill1)
print(bill2)
