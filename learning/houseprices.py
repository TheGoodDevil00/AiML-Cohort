import numpy as np  
import matplotlib.pyplot as plt

area=np.array([340,450,550,650,740])
price=([110,230,300,560,670])

m, c = np.polyfit(area,price,1)
x_val=int(input("Enter the area of house: "))
y_pred=x_val*m+c
print("The predicted price is: ",y_pred)

y_line= m*area+c
plt.scatter(area,price,color='Red',label='actual data')
plt.plot(area,y_line,color='green',label=f'Best fit line y= {m:.2f}x + {c:.2f}')

plt.xlabel("Area of Houses (dep var)")
plt.ylabel("Price of house (indep var)")
plt.title("House Price Model")
plt.legend()
plt.show()
