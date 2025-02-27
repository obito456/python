import numpy as np
import matplotlib.pyplot as plt

data=np.random.normal(0,5,100)
print(data)
plt.hist(data,5)
plt.show()
