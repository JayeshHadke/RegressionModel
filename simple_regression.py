#importing essential libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#reading .csv file
data = pd.read_csv('Book1.csv')

#extracting values on each column into array
X = data['Year'].values
Y = data['Salary'].values

#computing mean of X and Y values, and length of the given list of values
mean_x=np.mean(X)
mean_y=np.mean(Y)
n=len(X)

#computing a value of intercept(c) and slope(m) - coefficients
numer = 0
denom = 0
for i in range(n):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
m = numer / denom
c = mean_y - (m * mean_x)
print("Coefficients Slope and Intercept")
print(m, c) 
print('Which is in the form of y = m x + c')
print('y = '+str(m)+' * x + '+str(c))



max_x = np.max(X) 
min_x = np.min(X) 
 
# Calculating line values x and y
x = np.linspace(max_x,min_x, n)
y = c + m * x
 
# Ploting Line
plt.plot(x, y, color='#58b970', label='Regression Line')
# Ploting Scatter Points
plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')
 
plt.xlabel('Years')
plt.ylabel('Salary')
plt.legend()
plt.show()

#evaluation of parameters by root mean squares errors (RMSE)
rmse = 0
for i in range(n):
    y_pred = c + m * X[i]
    rmse += (Y[i] - y_pred) ** 2
rmse = np.sqrt(rmse/n)
print("RMSE")
print(rmse)