'''
Exercise 5.1: Fill lists with function values
'''
import matplotlib.pyplot as plt

from math import exp, pi,sqrt
def f(x):
	y=(1/sqrt(2*pi))*exp(-0.5*x**2)
	return y
initial=-4
h=8./40
xlist=[initial+i*h for i in range(41)]
ylist=[f(x) for x in xlist]
for x,y in zip(xlist,ylist):
	print(round(x,2),"\t",round(y,2))

plt.plot(xlist,ylist)
plt.show()
