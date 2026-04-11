import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([17,25,33,45.5]) #diameter in cm
y = np.array([126,343.9,427.9,835.3]) #price in INR

m, c = np.polyfit(x, y, 1)

# prediction for a new value
x_val = int(input("Enter size of pizza: "))
y_pred = m*x_val + c
print("Predicted value:", y_pred)

# regression line values
y_line = m*x + c

plt.scatter(x, y, color='blue', label='Actual data')
plt.plot(x, y_line, color='red', label=f'Best fit line: y = {m:.5f}x + {c:.5f}')

plt.xlabel("X (independent variable)")
plt.ylabel("Y (dependent variable)")
plt.title("Linear Regression in NumPy")
plt.legend()

plt.show()