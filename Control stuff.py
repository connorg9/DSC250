#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 09:19:20 2025

@author: connorgood
"""


x = list(range(1,101))
print(x)

total = 0

for i in x:
    total += i**(0.5)

print(total)

#%%

fib = [1,1]
n = 10

for i in range(n-2):
    fib.append(fib[-1] + fib[-2])

print(fib)

#%%

x = ["FBI", "CIA", "NBA", "NFL", "MLB"]

for acronym in x:
    
    a = ''
    
    for letter in acronym:
        
        a += letter+"."
        
    print(a)
    
#%%

n = 100
even = 0
odd = 0
for i in range(n):
    if i % 2 == 0:
        even += i
    else:
        odd += i
        
print(even)
print(odd)