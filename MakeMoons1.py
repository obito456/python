from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

x,y=make_moons(n_samples=100,noise=0.1)

plt.scatter(x[:,0],x[:,1],s=50,color='g')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
plt.clf()
