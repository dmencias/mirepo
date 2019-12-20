# -*- coding: utf-8 -*

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,10,0.1)
y=2*np.sin(4*x)-x**2+10*x  #f(x)=2sin(4x)-x^2+10x
plt.plot(x,y)
plt.show()


import datetime
oTime=datetime.datetime.now()
print(oTime.date())

from platform import platform

print(platform())
print(platform(1))
print(platform(0,1))