from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")
x,y=make_blobs(n_samples=100,centers=5,cluster_std=1,n_features=2)

plt.scatter(x[:,0],x[:,1],s=10,color='g')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
plt.clf()
