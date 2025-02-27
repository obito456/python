import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

onion = np.array([1,2,5,10]).reshape(-1, 1)
price = np.array([30,50,100,180])
model = LinearRegression()
model.fit(onion,price)

predict = model.predict([[6]])
print("Predicted price:", predict[0])

plt.scatter(onion, price, color='blue', label='Actual data')
plt.plot(onion, model.predict(onion), color='red', label='Regression Line')
plt.xlabel("onion (kg)")
plt.ylabel("Price")
plt.legend()
plt.show()
