import matplotlib.pyplot as plt
import numpy as np
def relu(x):
    return max(0,x)
x=(np.arange(-4,3,2,5))
y=[relu(i)for i in x]
plt.plot(x,y)
plt.show()
