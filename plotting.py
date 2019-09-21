import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,100)
y =32.79227055610875*x-23.300742285042617 
plt.plot(x, y, '-r', label='y =32.79227055610875*x-23.300742285042617 ')
plt.title('Graph of y =32.79227055610875*x-23.300742285042617 ')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()
