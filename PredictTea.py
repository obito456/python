import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

Tea=15
std=5
count=5
predict=np.random.normal(Tea,std,count).astype('int')
plt.figure(figsize=(8,5))
sb.histplot(predict,bins=30,kde=True,color="blue")

plt.xlabel("Predicted Tea Values")
plt.ylabel("Frequency")
plt.title("Normal Distribution of Predicted Tea Values")
plt.grid(True)
plt.show()
