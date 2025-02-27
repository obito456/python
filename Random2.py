import numpy as np
import matplotlib.pyplot as plt

data=np.random.uniform(0,5,100)
print(data)
plt.hist(data,10)
plt.show()
