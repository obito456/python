import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error

data={
    "size":[750, 800, 850, 900, 950, 1000,],
    "price":[150000, 160000, 170000, 180000, 190000, 200000]
}
dt=pd.DataFrame(data)
#print(dt.head())

x=dt[["size"]]
y=dt["price"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)

slope=model.coef_[0]
intercept=model.intercept_

print(f"slope : {slope}")
print(f"Intercept: {intercept}")

pred=model.predict(x_test)
print(x_test)

c_pred=pd.DataFrame({"Actual":y_test,"Predicted":pred})
print(c_pred)

mae=mean_absolute_error(y_test,pred)
mse=mean_squared_error(y_test,pred)
rmse=np.sqrt(mse)
print(mae)
print(mse)
print(rmse)
