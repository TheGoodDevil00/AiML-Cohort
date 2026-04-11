import numpy as np
import matplotlib.pyplot as plt

area=np.array([340,450,550,650,740])
price=np.array([110,230,330,460,570])

m=0 #initialise the slope val
c=0 #initialise the intercept val
me=np.mean(area)
ss=np.std(area)
# print(ss)
# print(me)
area = ((area-np.mean(area))/np.std(area))
# print(area)

alpha=0.01
n=len(area)

#implement a loop to obtain values of m and c
for i in range(50000):
  y_pred=m*area+c
  dm = (-2/n) * np.sum(area*(price-y_pred))
  dc = (-2/n) * np.sum(price-y_pred)
  m = m - alpha*dm
  c = c - alpha*dc
yline = m*area+c

sorted_index=np.argsort(area)

plt.scatter(area,price,color='red',label='Actual Data')
plt.plot(area[sorted_index],yline[sorted_index],color='green',label=f'Best fit line m:{m:.2f}, c:{c:.2f}')

plt.xlabel('Area of House')
plt.ylabel('Price of house')
plt.legend()
plt.show()