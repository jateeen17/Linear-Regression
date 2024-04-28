import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Simple Linear Regression\PerCapitaIncome.csv")

data = (data - data.mean())/data.std()
X = data['year'].values
Y = data['pci'].values

length = len(X)
x_mean = np.mean(X)
y_mean = np.mean(Y)

numerator = 0
denominator = 0

for i in range(length):
    numerator += ((X[i] - x_mean) * (Y[i] - y_mean))
    denominator += (X[i] - x_mean) ** 2
    
slope = numerator / denominator
intercept = (y_mean - (slope * x_mean))

print('SLOPE : ' + str(slope) + '\nINTERCEPT : ' + str(intercept))

x_max = np.max(X)
x_min = np.min(X)

x_plot = np.linspace(x_max, x_min, length)
y_plot = (slope * x_plot) + intercept

plt.xlabel('YEARS')
plt.ylabel('PCI')
plt.legend()
plt.plot(x_plot, y_plot, color = '#F4A950', label = 'Regression Line')
plt.scatter(X, Y, color = '#161B21', label = 'Scatter Plot')
plt.show()

rmse = 0
for i in range(length):
    y_predicted = slope * X[i] + intercept
    rmse += (Y[i] - y_predicted) ** 2
    
rmse = np.sqrt(rmse/length)
print('RMSE : ' + str(rmse))
