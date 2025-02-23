#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:23:23 2025

@author: connorgood
"""

a1 = 15.667
a2 = 17.23 
a3 = 0.75
a4 = 93.2

def energy(A, Z):
    if A % 2 == 1:
        a5 = 0
    elif A % 2 == 0 and Z % 2 == 0:
        a5 = 12.0
    elif A % 2 == 0 and Z % 2 == 1:
        a5 = -12.0
    B = (a1 * A) - (a2 * (A ** (2/3))) - (a3 * ((Z ** 2) / (A ** (1/3)))) - a4 * (((A - (2 * Z)) ** 2) / A) + (a5 / (A ** (1/2)))
    return (B / A)

def f(Z):
    l = []
    for A in range(Z, 3 * Z):
        l.append(energy(A, Z))
    return max(l)

def lots():
    maxes = []
    for Z in range(1, 101):
        maxes.append(f(Z))
    return maxes
    
#%%
print("The binding energy is:", energy(58, 28))

print(f(28))

for i in lots():
    if i == max(lots()):
        print(lots().index(i)+1)
    
slopes = []
for i in range(1, 100):
   slopes.append(lots()[i] - lots()[i-1]) 
   
for i in slopes:
    if i == max(slopes):
       print("The highest slope is", max(slopes), "at", slopes.index(i)+1)
    
    
    
#%%
import matplotlib.pyplot as plt

plt.plot(lots(), color = "m", marker = "d", lw = 0.5, ms = 2)
plt.ylabel("max B/A")
plt.xlabel("Z")
plt.grid()
plt.show()
















