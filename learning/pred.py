import numpy as np  
import matplotlib.pyplot as plt 

x = np.array([2,3,4,5,8,9,13,20])
y = np.array([11,12,15,17,22,27,30,25])

m,c = np.polyfit(x,y,1)
x_pred = int(input("Enter: "))
y_pred = m*x_pred + c
print("Predicted value is:", y_pred)
y_line = m*x + c

plt.scatter(x,y,color = 'red',label = 'actual data')
plt.plot(x,y_line , color = 'green', label = f'Best fit line: y{m:.2f} x{c:.2f}')
plt.xlabel("Dependent variable")
plt.ylabel("Independent variable")
plt.title("Regression model")
plt.legend()
plt.show()

