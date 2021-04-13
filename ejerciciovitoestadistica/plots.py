from main_1 import x, y
from main_2 import x1, y1
import matplotlib.pyplot as plt

# x1 = [10,20,30,40,50,60,70]
# y1 = [10000,20000,30000,40000,50000,60000,70000]

plt.plot(x,y,'g-',label='COVID-19',)
plt.ylabel('Casos confirmados')
plt.xlabel('Dias')
plt.plot(x1,y1,'m',label='COVID-19_2')
plt.legend()
plt.show()