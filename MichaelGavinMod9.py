#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random


guesses = 0

number = random.randint(-100, 100)

print("I am thinking of a number between -100 and 100. Can you guess in 7 attempts?")

while guesses < 7:
    print("Answer:")
    g = input()
    g = int(g)
    
    guesses = guesses + 1
    
    if g > number:
        print("Too High")
        
    if g < number:
        print("Too Low")
        
    if g == number:
        break
        
if g == number:
    guesses = str(guesses)
    print("Congratulations! You guessed my number in " + guesses + " attempts!")
        
if g != number:
    number = str(number)
    print("Sorry, the number I am thinking of is " + number + ".")

