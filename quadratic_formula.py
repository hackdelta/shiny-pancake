# -*- coding: utf-8 -*-2
"""
Created on Mon Jul  2 15:04:03 2018

@author: justi
"""
import math
letters = ['a','b','c']
coefficient = {}

n = 0
while(n < 3):
    letter_coefficient = letters[n] #set the variable 'letter_coefficient' to the letter at index n
    message = "Enter your '{}' value: ".format(letter_coefficient) #output for step 1: "Enter your a value"
    value = int(input(message)) #change the string input into an int
    coefficient[letters[n]] = value #add to the dictonary
    n+=1

def quadratic_formula(a, b, c):
    discriminant = (b**2) - (4*a*c)
    if discriminant < 0:
        return"The quadratic equation has no solutions"
    else:
        root_1 = (-b + math.sqrt(discriminant)) / (2*a)
        root_2 = (-b - math.sqrt(discriminant)) / (2*a)
        if discriminant > 0: 
            return "The quadratic equation has two solutions: x={}, and x={}".format(root_1, root_2)
        else: 
            return"The quadratic equation has one solutions: x={}".format(root_1)
    
print(quadratic_formula(coefficient['a'], coefficient['b'], coefficient['c']))
