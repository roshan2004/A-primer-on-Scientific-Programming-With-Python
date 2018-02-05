'''
Exercise 5.2: Fill arrays; loop version
'''

import matplotlib.pyplot as plt

from math import exp, pi,sqrt
xlist=[]

ylist=[]
initial=-4
h=8./41
for i in range(42):
	final=-4+i*h
	xlist.append(final)
for x in xlist:
	y=(1/sqrt(2*pi))*exp(-0.5*x**2)
	ylist.append(y)
plt.plot(xlist,ylist)
plt.show()
