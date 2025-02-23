#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:26:29 2025

@author: connorgood
"""
import matplotlib.pyplot as plt
import numpy as np
import random as r


left = np.ones(10000)
right = np.zeros(10000)

left_count = []
right_count = []

while abs(np.count_nonzero(left) - np.count_nonzero(right)) / 10000 >= .05:
    
    selected = r.randint(0, 9999)
    
    if left[selected] == 1:
        
        left[selected] = 0
        right[selected] = 1
        
    elif right[selected] == 1:
        
        left[selected] = 1
        right[selected] = 0
        
    left_count.append(np.count_nonzero(left))
    right_count.append(np.count_nonzero(right))
    

plt.figure()
plt.plot(left_count)
plt.plot(right_count)
plt.ylabel("Count of Particles")
plt.xlabel("Time (Iterations)")
plt.axhline(10000 / 2)
plt.show()

#%%

import matplotlib.pyplot as plt
import numpy as np
import random as r

N = 10000
left = np.ones(N)
right = np.zeros(N)
x = 0.25
time = 0

left_count = []
right_count = []
left_p = []
right_p = []

while time < 100000:
    
    left_pressure = np.count_nonzero(left) / x
    right_pressure = np.count_nonzero(right) / (1 - x)

    left_norm = left_pressure / (left_pressure + right_pressure)
    right_norm = right_pressure / (left_pressure + right_pressure)
    
    prob = r.random()

    selected = r.randint(0, N -1)
    
    if prob < left_norm:
        left[selected] = 0
        right[selected] = 1
        
    elif prob > left_norm:
        left[selected] = 1
        right[selected] = 0
        
    elif prob == left_norm or prob == right_norm:
        print("Wow this was unlikely")
        continue
        
    left_count.append(np.count_nonzero(left))
    right_count.append(np. count_nonzero(right))
    
    left_p.append(left_pressure)
    right_p.append(right_pressure)
    
    time += 1
    if abs(left_pressure - right_pressure) / (left_pressure + right_pressure) <= 0.05:
        break
    

plt.figure()
plt.plot(left_count)
plt.plot(right_count)
plt.ylabel("Pressure")
plt.xlabel("Time (Iterations)")
plt.show()

