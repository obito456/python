import numpy as np
import matplotlib.pyplot as plt

onion=[1,2,5,10]
price=[30,50,100,180]

plt.bar(onion,price,color='skyblue')
plt.xlabel("kg")
plt.ylabel("price")
plt.title("price analysis")
plt.grid(axis="y",linestyle="--",alpha=0.7)
plt.show()
