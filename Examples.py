#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:21:43 2025

@author: connorgood
"""

a = [2, 4, 10, 6, 8, 4]
n = []
min(a) 
max(a)
for i in a:
    n.append((i-min(a)) / (max(a) - min(a)))
n

#%%
import math

c = 0.01
ka = 1.78 * (10 ** -5)
tol = 1
h = [0]
i = 0

while tol > 1.e-10:
    h.append(math.sqrt(ka * (c - h[i])))
    tol = abs(h[i+1] - h[i])
    i += 1

pH = -math.log10(h[i])
pH

#%%

import numpy as np

card1 = np.random.randint(1,12)
card2 = np.random.randint(1,12)

while card1 or card2 <= 21:
    
    in1 = input("Player 1 action: draw, stay, quit")
    in2 = input("Player 2 action: draw, stay, quit")
    
    if in1 or in2 == "quit":
        break
    else:
        if in1 == "draw":
            card1 += np.random.randint(1,12)
        if in2 == "draw":
            card2 += np.random.randint(1,12)
        if in1 == "stay":
            pass
        if in2 == "stay":
            pass
    print("Player 1 value: ", card1)
    print("Player 2 value: ", card2)
    print("New round")
    
    
    

