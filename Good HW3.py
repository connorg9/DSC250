#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:28:48 2025

@author: connorgood
"""

#Q2.4.7 
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
hours = [44.7, 65.4, 101.7, 148.3, 170.9, 171.4, 176.7, 186.1, 133.9, 105.4, 59.6, 45.8]

x = list(zip(hours, months))
x.sort(reverse = True)
print("{}".format(x))

#%%

#P2.4.1

l = [1, 2, 3, 4]
total = 1
for i in l:
    total *= i

output = [total // num for num in l]
output
    
#%%

#P2.4.6 

n = 7
doublefac = 1
i = 1

if n%2 == 1:
    while (2*i)-1 <= n:
        doublefac *= (2*i)-1
        i += 1
print(doublefac)
        
#%%

#P2.4.7

n = 500
fib = [1,1]
b = [0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]
one_count = two_count = three_count = four_count = five_count = six_count = seven_count = eight_count = nine_count = 0
for i in range(2, n+1):
    fib.append(fib[i-1] + fib[i-2])
#fib is now huge dont print it (again)

for i in fib:
    x = int(str(i)[0])
    if x == 1:
        one_count += 1
    if x == 2:
        two_count += 1
    if x == 3:
        three_count += 1
    if x == 4:
        four_count += 1
    if x == 5:
        five_count += 1
    if x == 6:
        six_count += 1
    if x == 7:
        seven_count += 1
    if x == 8:
        eight_count += 1
    if x == 9:
        nine_count += 1
        
print("1: ", one_count / n, "\tBenford: ", b[0], "difference: {:.5f}".format((one_count / n) - b[0]))
print("2: ", two_count / n, "\tBenford: ", b[1], "difference: {:.5f}".format((two_count / n) - b[1]))
print("3: ", three_count / n, "\tBenford: ", b[2], "difference: {:.5}".format((three_count / n) - b[2]))
print("4: ", four_count / n, "\tBenford: ", b[3], "difference: {:.5f}".format((four_count / n) - b[3]))
print("5: ", five_count / n, "\tBenford: ", b[4], "difference: {:.5f}".format((five_count / n) - b[4]))
print("6: ", six_count / n, "\tBenford: ", b[5], "difference: {:.5f}".format((six_count / n) - b[5]))
print("7: ", seven_count / n, "\tBenford: ", b[6], "difference: {:.5f}".format((seven_count / n) - b[6]))
print("8: ", eight_count / n, "\tBenford: ", b[7], "difference: {:.5f}".format((eight_count / n) - b[7]))
print("9: ", nine_count / n, "\tBenford: ", b[8], "difference: {:.5f}".format((nine_count / n) - b[8]))


