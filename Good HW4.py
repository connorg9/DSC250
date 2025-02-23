#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 20:25:31 2025

@author: connorgood
"""
import numpy as np
import random
import matplotlib.pyplot as plt
#%%

#Q2.5.2

a = 1
b = np.sqrt(2)
a_new = []
b_new = []
diff = 100

while diff > 0.0000001:
    a_new.append((1/2) * (a + b))
    b_new.append(np.sqrt(a * b))
    a = a_new[-1]
    b = b_new[-1]
    diff = abs(a - b)
    print("New Iteration")
        
print("Gauss' contant is approximately", a)
#This could also be b, but since they have converged you only need to print one
plt.plot(a_new, label = "a")
plt.plot(b_new, label = "b")
plt.xlabel("iterations")
plt.ylabel("Values of A and B")
plt.legend(loc = "best")
plt.show()

#%%

#P2.5.8

n = list(range(2, 10001))
p = 2 
prime_numbers = []

while p <= 10000:
    
    for i in range(2 * p, 10001, p):
        if i in n:
            n[n.index(i)] = 0 #mark composites
    
    new = p + 1 #iterate in next loop
    found = False #have not found next iteration value
    
    while new <= 10000 and not found: #while within the bounds to find primes and haven't found a new prime
        
        if new in n and n[n.index(new)] != 0: #if new value is within n not marked in the list 
            found = True #yay! Use this new value
            p = new
        else:
            new += 1 #try again :(
    
    if not found: #if there are no more numbers less than 10000, stop the loop
        break
    
for i in n: 
    if i != 0: 
        prime_numbers.append(i)

print(prime_numbers) #printing all the primes takes a while, only do the first few

#%%

#P2.5.10
x_points = []
y_points = []
colors = []
x = []
y = []
inside = 0
n = 1000000 #choose a really big number here, 10,000 still gets inconsistent results

for i in range(n):
    
    x_points.append(random.random())
    y_points.append(random.random())

    if (x_points[i] ** 2) + (y_points[i] ** 2) <= 1:
        inside += 1
        colors.append('b')
    else:
        colors.append('r')
        
    
print("Pi approximation:", (inside / n) * 4)

for i in np.linspace(0, 1, 1000):
    y.append((1 - (i ** 2))** 0.5)
    x.append(i)
    

fig = plt.figure()
ax = plt.subplot(111)
plt.plot(x, y, color = "k", lw = 2)
plt.scatter(x_points[:1000], y_points[:1000], color = colors[:1000], alpha = 0.5)
ax.set_aspect("equal")
plt.show()
    
#%%

#HW 4-4 Game

colors = ["red", "green", "blue", "yellow", "purple"] #list of colors for the game

p1_tokens = [False, False, False, False, False]       #each players list of tokens
p2_tokens = [False, False, False, False, False]

while not all(p1_tokens) or all(p2_tokens):           #while there is a False in either list of tokens
    
    x = input("Player 1 action (draw or exit)")
    
    if x.lower() == "exit":         #I'll be using x,z,etc.lower() to make sure that the input matches the expected string
        print("Exiting the game")
        break
        
    y = input("Player 2 action (draw or exit)")
    
    if y.lower() == "exit":
        print("Exiting the game")
        break

    p1_spin = random.randint(1,9) #spin functionality
    p2_spin = random.randint(1,9)
    
    if p1_spin <= 5:                  #if spin is between 1-5
        index = p1_spin - 1           #index the spin value (indicies start at 0, so - 1) 
        if p1_tokens[index] == True:  #if that index in the tokens list is already there
            print("Player 1 already has", colors[index], ", sorry!")
        else:
            print("Player 1 got a ", colors[index], "token!")
            p1_tokens[index] = True
        
    if p1_spin == 6:
        z = input("Player 1, select a token color to add")
        
        if z.lower() == "red":
            p1_tokens[0] = True
        if z.lower() == "green":
            p1_tokens[1] = True
        if z.lower() == "blue":
            p1_tokens[2] = True
        if z.lower() == "yellow":
            p1_tokens[3] = True
        if z.lower() == "purple":
            p1_tokens[4] = True
            
        #the above section simply compares the user input to a color and sets that respective index to true


    if p1_spin == 7:
        z = input("Player 1, choose a token to steal from Player 2")
        
        if z.lower() == "red":
            if p2_tokens[0] == False:
                print("Player 2 didnt have a red token to steal!")
            elif p1_tokens[0] == True:
                print("Player 1 already has a red token!")
            else:
                p1_tokens[0] = True
                p2_tokens[0] = False
                
        if z.lower() == "green":
            if p2_tokens[1] == False:
                print("Player 2 didnt have a green token to steal!")
            elif p1_tokens[1] == True:
                print("Player 1 already has a green token!")
            else:
                p1_tokens[1] = True
                p2_tokens[1] = False
                
        if z.lower() == "blue":
            if p2_tokens[2] == False:
                print("Player 2 didnt have a blue token to steal!")
            elif p1_tokens[2] == True:
                print("Player 1 already has a blue token!")
            else:
                p1_tokens[2] = True
                p2_tokens[2] = False
                
        if z.lower() == "yellow":
            if p2_tokens[3] == False:
                print("Player 2 didnt have a yellow token to steal!")
            elif p1_tokens[3] == True:
                print("Player 1 already has a yellow token!")
            else:
                p1_tokens[3] = True
                p2_tokens[3] = False
                
        if z.lower() == "purple":
            if p2_tokens[4] == False:
                print("Player 2 didnt have a purple token to steal!")
            elif p1_tokens[4] == True:
                print("Player 1 already has a purple token!")
            else:
                p1_tokens[4] = True
                p2_tokens[4] = False
        
        #the above section again compares the input to a color string, and then checks if the player
        #to be stolen from actually has that token, as well as checking the current players tokens 
        #to make sure they do not have one of those already. Otherwise, it sets the current players
        #repective index to true, and the other players to false.
        
    if p1_spin == 8:
        print("Player 1 loses their turn!")
    
    if p1_spin == 9:
        lose = random.randint(0,4)  #if the spin is 9, then I want a random index from 0-4
        if p1_tokens[lose] == False:  #if the player didn't have that token, then output a string with the color the token to lose was
            print("Player 1 stinks, and doesn't even have a", colors[lose], "token to lose!")
        else:
            print("Player 1 lost a", colors[lose], "token!")
            p1_tokens[lose] = False  #set the index to false if they did have the token
    
    
    
    #repeat all of player 1 actions for player 2 (with names and variables switched) below
    
    if p2_spin <= 5:
        index = p2_spin - 1
        if p2_tokens[index] == True:
            print("Player 2 already has", colors[index], ", sorry!")
        else:
            print("Player 2 got a ", colors[index], "token!")
            p2_tokens[index] = True
        
    if p2_spin == 6:
        z = input("Player 2, select a token color to add")
        
        if z.lower() == "red":
            p2_tokens[0] = True
        if z.lower() == "green":
            p2_tokens[1] = True
        if z.lower() == "blue":
            p2_tokens[2] = True
        if z.lower() == "yellow":
            p2_tokens[3] = True
        if z.lower() == "purple":
            p2_tokens[4] = True
        
    if p2_spin == 7:
        z = input('Player 2, choose a token to steal from Player 1')
        
        if z.lower() == "red":
            if p1_tokens[0] == False:
                print("Player 1 didnt have a red token to steal!")
            elif p2_tokens[0] == True:
                print("Player 2 already has a red token!")
            else:
                p2_tokens[0] = True
                p1_tokens[0] = False
                
        if z.lower() == "green":
            if p1_tokens[1] == False:
                print("Player 1 didnt have a green token to steal!")
            elif p2_tokens[1] == True:
                print("Player 2 already has a green token!")
            else:
                p2_tokens[1] = True
                p1_tokens[1] = False
                
        if z.lower() == "blue":
            if p1_tokens[2] == False:
                print("Player 1 didnt have a blue token to steal!")
            elif p2_tokens[2] == True:
                print("Player 2 already has a blue token!")
            else:
                p2_tokens[2] = True
                p1_tokens[2] = False
                
        if z.lower() == "yellow":
            if p1_tokens[3] == False:
                print("Player 1 didnt have a yellow token to steal!")
            elif p2_tokens[3] == True:
                print("Player 2 already has a yellow token!")
            else:
                p2_tokens[3] = True
                p1_tokens[3] = False
                
        if z.lower() == "purple":
            if p1_tokens[4] == False:
                print("Player 1 didnt have a purple token to steal!")
            elif p2_tokens[4] == True:
                print("Player 2 already has a purple token!")
            else:
                p2_tokens[4] = True
                p1_tokens[4] = False
        
        
    if p2_spin == 8:
        print("Player 2 loses their turn!")
    
    if p2_spin == 9:
        lose = random.randint(0,4)
        if p2_tokens[lose] == False:
            print("Player 2 stinks, and doesn't even have a", colors[lose], "token to lose!")
        else:
            print("Player 2 lost a", colors[lose], "token!")
            p2_tokens[lose] = False



    for i in range(len(colors)): #for each index in however long the colors list is (I couldve used 0-4 like I had been, but this felt more professional)
        if p1_tokens[i] == True:                                #if the player has that token
            print("\t\t\t\t\t\t\t\tPlayer 1 has:", colors[i])
    if not any(p1_tokens):                                      #if all of the elements in the token list are False
        print("\t\t\t\t\t\t\t\tPlayer 1 has no tokens!")

    
    for j in range(len(colors)):
        if p2_tokens[j] == True:
            print("\t\t\t\t\t\t\t\t\t\t\tPlayer 2 has:", colors[j])
    if not any(p2_tokens):
        print("\t\t\t\t\t\t\t\t\t\t\tPlayer 2 has no tokens!")

    #I used a bunch of tabs here because while playing, it got a bit difficult to see who had what, and what was happening
    
    if all(p1_tokens): #if all of the elements in the token list are true
        print("Player 1 wins!")
        break
    
    if all(p2_tokens):
        print("Player 2 wins!")
        break
    
    if all(p1_tokens) and all(p2_tokens): #if all elements in both token lists are true
        print("It's a tie!")
        break
    
    print("New round") #if nobody wins, I want this to be the last thing that happens before another iteration of the loop





    

