import numpy as np

data=np.array([[10,20,30],[40,50,60]])
res1=np.var(data,axis=0)
res2=np.var(data,axis=1)
print(res1)
print(res2)
