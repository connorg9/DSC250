#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:25:26 2025

@author: connorgood
"""
import random as r
import matplotlib.pyplot as plt
#%%

wins = []
losses = []
x = 0

while x < 10001:
    
    location = r.randint(0, 2)
    doors = [False, False, False]
    
    doors[location] = True
    
    choice = r.choice([0, 1, 2])
    
    for i in doors:
        if doors[i] == False and doors[i] != doors[choice]:
            doors.remove(r.randint(0,1))
            break
    
    if choice == location:
        wins.append(True)
    else:
        losses.append(True)
        
    x += 1

print("If you stay, you win {0:.2f}% of the time".format((len(wins) / 10000) * 100))

#%%

wins = []
losses = []
x = 0

while x < 10001:
    
    location = r.randint(0, 2)
    doors = [False, False, False]
    
    doors[location] = True
    
    choices = [0, 1, 2]
    choice = r.choice(choices)
    
    for i in doors:
        if doors[i] == False and doors[i] != doors[choice]:
            gone = r.randint(0,1)
            doors.remove(gone)
            choices.remove(gone)
            break
    
    choice = r.choice(choices)
        
    if choice == location:
        wins.append(True)
    else:
        losses.append(True)
        
    x += 1

print("If you stay, you win {0:.2f}% of the time".format((len(wins) / 10000) * 100))
    
#%%

x = 0
N = [int(1E6)]
p = 0.05

while N[-1] > 0:
    
    decays = 0
    
    for i in range(N[-1]):
        prob = r.random()
        if prob <= p:
            decays += 1
    
    N.append(N[-1] - decays)

plt.figure()

plt.subplot(211)
plt.plot(N)
plt.xlabel("Iterations")
plt.ylabel("Particles left")

plt.subplot(212)
plt.semilogy(N)
plt.xlabel("Iterations")
plt.ylabel("Particles left")

plt.show()
    















