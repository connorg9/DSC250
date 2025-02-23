#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:27:36 2025

@author: connorgood
"""

import numpy as np
import matplotlib.pyplot as plt
#%%

#P3.1.1

f1 = []
f2 = []
x = [] 

for i in np.linspace(-20, 20, 1000):        #create a "smooth" graph from -20 to 20
    f1.append(np.log(1 / (np.cos(i) ** 2))) 
    f2.append(np.log(1 / (np.sin(i) ** 2)))
    x.append(i)
    

plt.plot(x, f1, label = "cos") #plot the first function w/ x points and function values, include label
plt.plot(x, f2, label = "sin") #same as above, with sin
plt.xlabel("X value")
plt.ylabel("Function value")
for i in range(-12, 13):     #for values between -12 and 12 (will be multiplied by pi) [found through guess and check]
    plt.vlines(i * (np.pi / 2), 0, 14, lw = 0.5, color = "m") #graph vertical lines to better see the multiples of pi
plt.legend(loc = "best")
plt.show()

"""
At 0, π/2, π, etc, each graph has a peak, offset by one. For example, f2 has a peak at 0, ±π,  
while f1 has peaks at ±π/2. The peaks of f1 form a "dish" or "bowl" shape, and f2 is inverted, 
shaped like a dome. 
"""

#%%

#P3.3.1 

radius_1 = []
radius_2 = []
theta = []

def spiral(a, b, t): #create a function for the first spiral
    r = a + (b * t)
    return r

def log_spiral(a, t): #same as above w/ different calculation of r
    r = a ** t
    return r

for i in np.linspace(0, 8 * np.pi, 1000): #"smooth" graph from 0 to 8π 
    radius_1.append(spiral(0, 2, i))
    radius_2.append(log_spiral(0.8, i))
    theta.append(i)
    
    
ax1 = plt.subplot(121, projection = "polar") #use polar projection to graph, subplot 1 in the grid
ax1.plot(theta, radius_1)
ax2 = plt.subplot(122, projection = "polar") #same as above, subplot 2
ax2.plot(theta, radius_2)
plt.show()


#%%

#P2.7.5 (again)

g = 9.81

def motion(v, a):
    a = a * (np.pi / 180)
    r = (v**2 * np.sin(2 * a)) / g
    h = (v**2 * ((np.sin(a)) ** 2)) / (2 * g)
    return r, h

ranges = []
heights = []
thetas = []
for i in np.linspace(0, 90, 1000): #again, "smooth" graph from 0 to 90 degrees
    r, h = (motion(10, i)) #since function returns tuple, assign variables to each in return
    ranges.append(r)       #append the r to ranges
    heights.append(h)      #append h to heights
    thetas.append(i)

plt.plot(thetas, ranges, label = "Range")
plt.plot(thetas, heights, label = "Heights")
plt.legend(loc = "best")
plt.xlabel("Degrees")
plt.ylabel("Meters")
plt.show()



