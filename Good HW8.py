#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:00:39 2025

@author: connorgood
"""

#%%
def create_dict(file):
    
    D = {}
    planets = []
    f = open(file, "r")
    
    for i, line in enumerate(f):
        
        if i == 2:
            columns = line.strip().split("\t")
            
            for name in columns:
                planets.append(name.strip())
        
            for planet in planets:
                D[planet] = {}
            
        elif i > 2:
            data = line.strip().split("\t")
            labels = data[0].strip()
            
            for j, numbers in enumerate(data[1:]):
                
                if j < len(planets):
        
                    D[planets[j]][labels] = numbers
        
    return D
        
D = create_dict("/Users/connorgood/Downloads/planetary-fact-sheet.txt")
print(D["MARS"]["Ring System?"])
print(D["MARS"])

#%%

def provide_P(n):
    x = 0
    P = [1, 1, 1]
    
    while x <= n:
        
        for i in range(3, n):
            new = P[i - 2] + P[i - 3]
            P.append(new)
            x += 1
            
    return P


def provide_Q(n):
    x = 0
    Q = [3, 0, 2]
    
    while x <= n:
        for i in range(3, n):
            new = Q[i - 2] + Q[i - 3]
            Q.append(new)
            x += 1

    return Q

p_set = set(provide_P(10000))
q_set = set(provide_Q(10000))

print("There are {0} unique integers in P up to n = 10000".format(len(p_set)))
print("There are {0} unique integers in Q up to n = 10000".format(len(q_set)))
print("The unique numbers that are in both P and Q are {0}".format(p_set & q_set))

primes = []
for i in range(1, 10000):
    for j in range(2, i):
        if j % i == 0:
            continue
        else:
            primes.append(i)
    
print("The unique prime numbers that occur in both are {0}".format(p_set & q_set & set(primes)))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    